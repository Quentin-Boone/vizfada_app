from django.core.management.base import BaseCommand, CommandError
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
import os
import scipy as scp
import fastcluster as fc
import json

from data.models import Correlation
from VizFaDa.settings.base import ASSETS

"""
ONTOLOGY_URL = "http://purl.obolibrary.org/obo/"
KEEP_COLUMNS = ["derivedFrom","experimentalProtocol","extractionProtocol",
                "files","libraryPreparationDate","libraryPreparationLocation",
                "material","organism_spec","organization","paperPublished",
                "project","publishedArticles","releaseDate","RNA-seq",
                "ChIP-seq DNA-binding","runs","sampleStorage","sampleStorageProcessing",
                "samplingToPreparationInterval","secondaryProject_exp",
                "sequencingDate","sequencingLocation","species","study",
                "submission","updateDate","accession","assayType","biosampleId",
                "cellSpecimen","cellType","experiment","poolOfSpecimens"]
"""

class Command(BaseCommand):
    help = 'Fill SQLite database with correlation tables, metadata and clustering'
    species = os.listdir(ASSETS)

    def add_arguments(self, parser):
        parser.add_argument('verbose', type=bool, nargs='?', default=False)

    def fill_species(self, verbose):
        print(self.species)
        for sp in self.species:
            exps = [d for d in os.listdir(os.path.join(ASSETS, sp))]
            #if exp=="ChIPSeq": index_col="experiment_accession"
            self.fill_experiment(sp, exps, verbose, index_col="experiment_accession")

    def fill_experiment(self, species, exps, verbose, index_col="run_accession"):

        for exp in exps:
            if verbose:
                print(f"{species} {exp}")

            expDir = str(os.path.join(ASSETS, species, exp))

            metaPath = expDir + "/metadata.tsv"
            corPath = expDir + "/correlation.csv"

            # Metadata
            with open(metaPath) as meta:
                metadata = pd.read_csv(meta, sep="\t", header=0, index_col=index_col)

            metadata.index=metadata["experiment_accession"]
            metadata["run_accession"]=[run["accession"] for run in metadata["run"]]
            runs=metadata["run_accession"].groupby(by="experiment_accession").agg(["unique"])
            files=metadata["id_file"].groupby(by="experiment_accession").agg(["unique"])

            meta=metadata.copy()
            metadata = metadata.applymap(str)
            excludedCols=[]
            for c in metadata.columns:
                counts=metadata[c].groupby(by=metadata.index).nunique()
                if max(counts)>1:
                    excludedCols.append(c)
            metadataTrimmed = meta.drop(excludedCols, axis=1)
            if verbose: print(f"Metadata columns: {metadataTrimmed.columns}")
            metadata = metadataTrimmed.drop_duplicates()
            if verbose: print("Kept {}/{} rows".format(len(metadata.index), len(metadataTrimmed.index)))


            # Correlation
            with open(corPath) as correlation:
                correlation = pd.read_csv(correlation, sep=",", header=0, index_col=0)

            # Clustering
            if verbose:
                print("Metadata and Correlation imported.\nClustering in progress.")
            dist = scp.spatial.distance.pdist(correlation)
            link = fc.linkage(dist, method="average")
            # link = scp.cluster.hierarchy.linkage(dist, method="average")
            if verbose:
                print("Clustering done. Optimal Leaf Ordering in progress")
            olo = scp.cluster.hierarchy.optimal_leaf_ordering(link, dist)

            c = Correlation(species=species, experiment=exp, correlation=expDir +
                            "/corPickle", metadata=expDir + "/metaPickle",
                            clustering = expDir + "/clusterPickle")

            # Pickling
            if verbose:
                print("OLO done.\nPickling dataframes and clustering.")

            c.pickle(correlation, "correlation")
            c.pickle(metadata, "metadata")
            c.pickle(olo, "clustering")

            c.save()
            
            # Experiments
            #if verbose: print("Saving experiments")
            #self.fill_experiment_table(spDir, verbose)
            #if verbose: print("Experiments saved")

            # All done
            if verbose:
                print("Saved %s." % (exp))
                
    """
    def fill_experiment_table(self, speciesDir, verbose):
        expDirs = next(os.walk('.'))[1]
        expDirs.remove("fastqc")
        for exp in expDirs:
            expPath = os.path.join(speciesDir, exp)
            fastqc = [os.path.abspath(os.path.join(speciesDir, 'fastqc', f))
                      for f in os.listdir(os.path.join(speciesDir, 'fastqc'))
                      if exp in f]
            quant = [os.path.abspath(os.path.join(expPath, f))
                     for f in os.listdir(expPath)
                     if "quant" in f]
            bigwig =
            exp = Experiment(id=exp)
            exp.set_json_field("files", {"fastqc": fastqc, "quant": quant})

            exp.save()
    """
    """
        for s in self.sizes:
            if verbose:
                print(str(s))
            try:
                os.mkdir("%s/%d" % (spDir, s))
            except FileExistsError:
                pass
            fig = sns.clustermap(correlation, figsize=(s, s))
            png = "%s/%d/clustermap.png" % (spDir, s)
            fig.savefig(png, transparent=False)
            i = Image(species=c, plot="%s/%s/figPickle" % (spDir, s),
                      size=s, png="%s/%d/clustermap.png" % (spDir, s))
            i.pickle(fig)
            i.save()
    """

    def handle(self, **options):
        self.fill_species(options['verbose'])
