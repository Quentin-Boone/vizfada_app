import pandas as pd
import pybedtools as pbt
import math
import scipy.stats as stats
import io

from utils.access_data import fetch_data, experiment_uri
from heatmap.heatmap import ClusteredHeatmap

def jaccard_user(userExp, clusteredHeatmap: ClusteredHeatmap, name="USER_FILE"):
    userExp = pbt.bedtool.BedTool(userExp, from_string=True)
    expList = {exp: pbt.bedtool.BedTool(fetch_data(f"{experiment_uri(exp)}/macs/{exp}_R1_peaks.narrowPeak"), from_string=True) for exp in clusteredHeatmap.get_metadata().keys}

    nExp = len(expList)
    correlations = pd.Series(list("".zfill(nExp + 1)), index = list(expList.keys()) + [name], name=name)
    correlations[name] = 1

    for expName, expBed in expList.items():
        correlations[expName] = expBed.jaccard(userExp)["jaccard"]
    
    clusteredHeatmap.add_correlation(correlations)
    return clusteredHeatmap



def jaccard_full(expList):
    """
    Create the correlation matrix between all the experiments processed with the vizfada chipseq pipeline.
    Saves the resulting table in the working directory.
    
    :param
    
    Output:
    - correlation matrix saved as a .csv file in the working directory    
    """
    all_narrow_peaks = {exp: pbt.bedtool.BedTool(fetch_data(f"{experiment_uri(exp)}/macs/{exp}_R1_peaks.narrowPeak"), from_string=True) for exp in expList}

    a = "".zfill(len(all_narrow_peaks))
    data = {exp: list(a) for exp in all_narrow_peaks.keys()}

    df = pd.DataFrame(data)
    df.index = df.columns

    nExp = df.shape[0]

    for i in range(nExp):
        expi = list(df.columns)[i]
        df[expi][expi] = 1
        for j in range(i+1, nExp):
            expj = list(df.index)[j]
            df[expi][expj] = all_narrow_peaks[expi].jaccard(all_narrow_peaks[expj])["jaccard"]
            df[expj][expi] = df[expi][expj]

    return df.to_csv()

def pearson(species, expList):
    """
    Create the correlation matrix between all the experiments processed with the vizfada chipseq pipeline.
    Saves the resulting table in the working directory.
    
    Keyword arguments:
    - species: the name of the species
    - path: the path to the 'results' directory created by the vizfada chipseq pipeline
    
    Output:
    - correlation matrix saved as a .csv file in the working directory
    """

    tpm = pd.read_csv(io.StringIO(fetch_data(f"species/{species}/rnaseq/salmon/salmon.merged.gene_tpm.tsv")), sep="\t", index_col=0)
    tpm = tpm.drop("gene_name", axis=1)
    tpm = tpm[expList]

    logtpm = tpm.applymap(lambda x: math.log10(x+1))
    a = "".zfill(logtpm.shape[1])
    data = {exp: list(a) for exp in logtpm.columns}

    df = pd.DataFrame(data)
    df.index = df.columns

    nExp = df.shape[0]
    for i in range(nExp):
        expi = list(df.columns)[i]
        df[expi][expi] = 1
        for j in range(i+1, nExp):
            expj = list(df.index)[j]
            df[expi][expj] = stats.pearsonr(logtpm[expi], logtpm[expj])[0]
            df[expj][expi] = df[expi][expj]
    
    return df.to_csv()