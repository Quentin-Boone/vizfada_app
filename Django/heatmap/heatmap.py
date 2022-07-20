import json
import typing
import os
import pickle

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import pandas as pd
import seaborn as sns
from distinctipy import distinctipy
import scipy as scp
import fastcluster as fc
from io import StringIO
from pathlib import Path


from django.conf import settings
from metadata.metadata import Metadata
from utils.access_data import fetch_data

from matplotlib.patches import Rectangle

import matplotlib
matplotlib.use('Agg')

Filters = typing.Mapping[str, typing.List]
Highlights = typing.Mapping[str, Filters]
"""
  Filters type example:
    {"cellType": ["blood", "brain"], "sex": ["female"]}

  Highlights type example:
    {"blue": {"project_name": ["GENESWITCH"]},
     "red": {
            "organism_id": ["id1", "id2"],
            "article_published": ["yes"]
            }
    }
"""

"""
DEFAULT_PALETTE = [
    [0, "#fcfae5"],
    [0.1, "#8fe0a8"],
    [0.2, "#52e8a6"],
    [0.3, "#1eccbd"],
    [0.4, "#0c89ae"],
    [0.5, "#faebdd"],
    [0.6, "#f37651"],
    [0.7, "#e13342"],
    [0.8, "#ad1759"],
    [0.9, "#701f57"],
    [1, "#03051a"]
]

DEFAULT_PLOTLY_PALETTE = {"colorscale": [
    [-1, "#085f79"],
    [-0.80, "#0c89ae"],
    [-0.60, "#1eccbd"],
    [-0.40, "#52e8a6"],
    [-0.20, "#8fe0a8"],
    [0.0, "#faebdd"],
    [0.20, "#03051a"],
    [0.40, "#e13342"],
    [0.60, "#03051a"],
    [0.80, "#03051a"],
    [1.0, "#03051a"]
]}
"""

DEFAULT_PALETTE = [
    [0.0, "#faebdd"],
    [0.20, "#f37651"],
    [0.40, "#e13342"],
    [0.60, "#ad1759"],
    [0.80, "#701f57"],
    [1.0, "#03051a"]
]

cmap = colors.LinearSegmentedColormap.from_list("", DEFAULT_PALETTE)
DEFAULT_SNS_OPTIONS = {"cmap": cmap}
DEFAULT_PLOTLY_PALETTE = {"colorscale": DEFAULT_PALETTE}


class ClusteredHeatmap:

    def __init__(self, species: str, exp: str, seaborn_options: dict,
                 force_clustering=False) -> None:
        print("Creating new ClusteredHeatmap")
        self.species = species
        self.experiment = exp
        self.root = f"species/{species}/{exp}"
        self.filters: Filters = {}
        self.highlights: Highlights = {}
        self._load_data(force_clustering)
        self.correlation = self.ALL_CORRELATION
        self.metadata = self.ALL_METADATA
        self.clustering = self.ALL_CLUSTERING
        self.seaborn_options = DEFAULT_SNS_OPTIONS.copy()
        self.seaborn_options.update(seaborn_options)
        self.fig = None
        self.highlighted = None
        self.annotated = ""
        self.annotation_legend = {}
        self.get_fields_and_count()
        self.plotly = {}

    def __str__(self) -> str:
        return "ClusteredHeatmap: \n\t{}\n\t{}\n\t{}\n\t{}\n\t{}".format(
                self.species, str(self.filters), str(self.highlights),
                self.annotated, str(self.seaborn_options))

    # Load data

    def _load_data(self, force_clustering) -> None:
        root = self.root
        self.ALL_METADATA = Metadata(
            json.loads(fetch_data(f"{root}/metadata.json")))
        self.ALL_CORRELATION = pd.read_table(StringIO(fetch_data(f"{root}/correlation.csv")), sep=",", header=0, index_col=0)
        self.ALL_CORRELATION = self.ALL_CORRELATION.reindex(
            [i for i in self.ALL_METADATA.keys
             if i in self.ALL_CORRELATION.index])
        self.ALL_CORRELATION = self.ALL_CORRELATION[list(
            self.ALL_CORRELATION.index)]
        self.correlation: pd.DataFrame = self.ALL_CORRELATION
        self.metadata = self.ALL_METADATA
        print("Loaded correlation for {} experiments and metadata for {} experiments".format(self.correlation.shape[0], len(self.metadata)))
        print("Creating new clustering...")
        self._cluster(force=True)
        self.ALL_CLUSTERING = self.clustering
        clustering = os.path.join(settings.DATA, "clusterings", f"{self.species}-{self.experiment}")
        path = Path(os.path.join(settings.DATA, "clusterings"))
        path.mkdir(parents=True, exist_ok=True)
        if os.path.exists(clustering) and not force_clustering:
            print("Loading existing clustering...")
            self.ALL_CLUSTERING = pickle.load(open(clustering, "rb"))
        else:
            print("Creating new clustering...")
            self._cluster(force=True)
            self.ALL_CLUSTERING = self.clustering
            pickle.dump(self.ALL_CLUSTERING, open(clustering, "wb"))

    # Add Experiment

    def add_correlation(self, correlations: pd.Series or pd.DataFrame):   
        self.correlation = pd.concat([self.correlation, correlations], axis=1, join="inner")
        self.correlation = self.correlation.T
        self.correlation = pd.concat([self.correlation, correlations], axis=1, join="inner")
        self.correlation = self.correlation.astype('float64')
        self._cluster(force = True)
        self.ALL_CLUSTERING = self.clustering
        if type(correlations) == pd.Series:
            names = [correlations.name]
        else:
            names = correlations.columns
        self.correlation[names] = self.correlation[names].apply(lambda x: -x)
        self.correlation = self.correlation.T
        self.correlation[names] = self.correlation[names].apply(lambda x: -x)


    # Get attributes

    def get_fields_and_count(self) -> dict:
        self.fields = self.metadata.fields_counts()
        return self.fields
    
    def get_fields_as_list(self) -> list:
        results = [dict(**{"field": k}, **v) for k, v in self.fields.items()]
        return results

    def get_heatmap(self, highlighted: bool = True) -> sns.matrix.ClusterGrid:
        if not highlighted:
            if not self.fig:
                self._draw_heatmap()
            return self.fig
        else:
            if not self.highlighted:
                self._highlight_fig()
            return self.highlighted

    def get_size(self):
        return self.correlation.shape[0]

    def get_metadata(self):
        return self.metadata

    def get_correlation(self):
        c = self._cluster()
        return c

    # Clustering

    def _cluster(self, force=False) -> None:
        if self.filters or force:
            print("Re-clustering...")
            dist = scp.spatial.distance.pdist(self.correlation)
            link = fc.linkage(dist, method="average")
            # olo = scp.cluster.hierarchy.linkage(dist, method="average",
            #                                     optimal_ordering=True)
            olo = scp.cluster.hierarchy.optimal_leaf_ordering(link, dist)
            self.clustering = olo
        else:
            print("No re-clustering necessary")
            self.clustering = self.ALL_CLUSTERING

        C = self.correlation
        # print(self.clustering)
        D = scp.cluster.hierarchy.dendrogram(self.clustering, no_plot=True)
        order = [self.correlation.columns[i] for i in D['leaves']]
        C = C[order]
        C = C.reindex(order)
        return(C)

    # Filtering methods

    def _filter_meta(self, filters: Filters) -> pd.DataFrame:
        print("Filtering metadata with filters %s" % (str(filters)))
        m = self.metadata
        self.metadata = m.filter(filters)
        print("Keeping %d samples" % (len(self.metadata)))
        return self.metadata

    def _filter_corr(self) -> None:
        print("Filtering correlations...")
        selected = [c for c in self.correlation.columns if c in self.metadata.keys]
        print(len(selected))
        self.correlation = self.correlation.loc[selected, selected]
        print("Keeping %s samples" % (self.correlation.shape[0]))

    def add_filters(self, filters: Filters) -> None:
        if not filters == {}:
            print("Adding filters...")
            for f, v in filters.items():
                print("%s %s" % (f, str(v)))
                self.filters.setdefault(f, [])
                self.filters.update(
                    {f: list(set(self.filters[f]).union(set(v)))})
            self._reset_view()
            self._update_view()

    def remove_filters(self, filters: Filters) -> None:
        print("Removing filters...")
        for f, v in filters.items():
            self.filters.setdefault(f, [])
            self.filters.update({f: list(set(self.filters[f]) - set(v))})
            if self.filters[f] == []:
                self.filters.pop(f)
        self._reset_view()
        self._update_view()

    # Highlighting method

    def _highlight_fig(self) -> None:
        print("Highlighting figure...")
        if not self.fig:
            self._draw_heatmap()
        fig = self.fig
        ax = fig.ax_heatmap
        n = self.correlation.shape[0]
        for color, runs in self.highlights.items():
            for run in runs:
                i = self.correlation.columns.tolist().index(run)
                i = fig.dendrogram_col.reordered_ind.index(i)
                ax.add_patch(Rectangle((0, i), n, 1, fill=True,
                             color=color, alpha=0.3, lw=0))
                ax.add_patch(Rectangle((i, 0), 1, n, fill=True,
                             color=color, alpha=0.3, lw=0))
            for xtick, ytick in zip(ax.get_xticklabels(), ax.get_yticklabels()):
                if xtick.get_text() in runs:
                    xtick.set_color(color)
                if ytick.get_text() in runs:
                    ytick.set_color(color)
        self.highlighted = fig

    def add_highlights(self, highlights: Highlights) -> None:
        if not highlights == {}:
            print("Adding highlights...")
            for color, filters in highlights.items():
                self.highlights.setdefault(color, {})
                runs = list(self._filter_meta(filters).to_dict().keys())
                self.highlights.update(
                    {color: list(set(self.highlights[color]).union(set(runs)))})
            self._highlight_fig()

    def remove_highlights(self, highlights: Highlights) -> None:
        print("Removing highlights...")
        for color, runs in highlights.items():
            self.highlights.setdefault(color, [])
            self.highlights.update(
                {color: list(set(self.highlights[color]) - set(runs))})
        self._highlight_fig()

    # Reset metadata and correlation table

    def _reset_view(self) -> None:
        print("Resetting metadata and correlations...")
        # [self.ALL_METADATA.experiment_accession.isin(self.ALL_CORRELATION.index)]
        self.metadata = self.ALL_METADATA
        self.correlation = self.ALL_CORRELATION

    def _update_view(self) -> None:
        print("Updating metadata and correlations...")
        self._filter_meta(self.filters)
        self._filter_corr()
#        self._draw_heatmap()

    # Annotation methods

    def _annotate(self) -> None:
        print("Annotating heatmap..")
        field = self.annotated
        try:
            print(f"Getting field {field} from metadata...")
            values = self.metadata.get_field(field)
        except KeyError:
            return None

        cor = self._cluster()
        print("Assigning colors to values for plotlyCheck...")
        valueslist = [values[exp] for exp in cor.index]
        match = dict(
            zip(set(valueslist), distinctipy.get_colors(len(set(valueslist)))))
        self.annotation_legend = match

        print("Assigning colors to values for seaborn...")
        valueslist = [values[exp] for exp in self.correlation.index]
        row_colors = [match[value] for value in valueslist]
        self.seaborn_options.update({"row_colors": row_colors})

    def annotate_field(self, field: str) -> None:
        self.get_fields_and_count()
        self.annotated = field
        self._annotate()

    # Draw Seaborn heatmap

    def _draw_heatmap(self) -> None:
        print("Drawing heatmap...")

        print(self.correlation)
        self._cluster()
        print(self.correlation)

        self.fig = sns.clustermap(self.correlation, row_linkage=self.clustering,
                                  col_linkage=self.clustering, **self.seaborn_options)

        self.highlighted = self.fig

    # Plotly

    def get_plotly_json(self):
        cor = self._cluster()
        #z=self.correlation.to_json(orient="values", )
        z = [cor[c].to_list() for c in cor.columns]
        z.reverse()
        x = cor.index.to_list()
        y = x.copy()
        y.reverse()
        result = {"z": z,
                  "x": x,
                  "y": y,
                  "yaxis": "y",
                  "xaxis": "x2",
                  "colorscale": DEFAULT_PLOTLY_PALETTE["colorscale"],
                  "type": "heatmap",
                  "hovertemplate": '<b>x</b> : %{x}<br><b>y</b> : %{y}<br><b>r</b> : %{z}<extra></extra>'
                  }
        if (self.annotated):
            values = self.metadata.get_field(self.annotated)
            metaX = [values[k] for k in x]
            metaY = metaX.copy()
            metaY.reverse()
            # print(metaY)
            # print(metaX)
            result["text"] = [[f'{x}<br>{y}' for x in metaX] for y in metaY]
            result["hovertemplate"] = '<b>x</b> : %{x}<br><b>y</b> : %{y}<br><extra><b>%{text}</b></extra>'
        # else:
            #result['hovertemplate']='<b>x</b> : %{x}<br><b>y</b> : %{y}<br><extra><b>%{text}</b></extra>'
        self.plotly = result
        return result

    def get_row_annotation(self, field):
        if (not self.annotated):
            return ''
        if (self.annotated != field and (list(self.legend.keys()) == self.fields[field])):
            self.annotate_field(field)
        print(f"Annotation for plotly: {field}")
        values = self.metadata.get_field(field)
        y = self.plotly["y"]
        legend = self.annotation_legend
        values = [values[k] for k in y]
        print(values)
        match = dict(zip(legend.keys(), range(len(legend))))
        z = [match[k] for k in values]
        z = [[v] for v in z]
        print(z)
        text = [[v] for v in values]
        legendPlotly = {n: legend[k] for k, n in match.items()}
        colorscale = [
            [value/(len(legend)-1), f"rgb({int(round(c[0]*255))},{int(round(c[1]*255))},{int(round(c[2]*255))})"] for value, c in legendPlotly.items()]
        return({"z": z,
               "x": [field],
                "y": y,
                "text": text,
                "yaxis": "y",
                "xaxis": "x",
                "colorscale": colorscale,
                "type": "heatmap",
                "showscale": False,
                "hovertemplate": '<b>y</b> : %{y}<br><extra><b>%{text}</b></extra>'})
