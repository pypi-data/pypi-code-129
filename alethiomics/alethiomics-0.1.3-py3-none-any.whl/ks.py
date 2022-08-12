"""Calculate Fisher's Statistics on two groups of cells, testing whether the number of expressed cells (not zero expression) has significantly changed between two groups.
"""
# imports
from scipy.stats import ks_2samp

def calc_ks_stats(adata, group_column, group_mutant, group_normal):
    # calculate KS statistics
    adata.var['ks-stat'] = 0
    adata.var['ks-pval'] = 1
    for gene in adata.var.index:
        d1 = adata[adata.obs[group_column] == group_mutant].to_df(layer="scvi_normalized")[gene]
        d2 = adata[adata.obs[group_column] == group_normal].to_df(layer="scvi_normalized")[gene]
        ks = ks_2samp(d1, d2)
        adata.var.loc[gene, 'ks-stat'] = ks[0]
        adata.var.loc[gene, 'ks-pval'] = ks[1]
    return(adata)
