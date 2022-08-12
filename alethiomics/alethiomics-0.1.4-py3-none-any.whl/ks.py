"""Calculate Kolmogorov-Smirnov's Statistics on two groups of cells, testing whether their expression distributions for a given gene are significantly different.
"""
# imports
from scipy.stats import ks_2samp

def calc_ks_stats(adata, group_column, group_mutant, group_normal, layer = None):
    """Calculate Kolmogorov-Smirnov's Statistics on two groups of cells.

    Parameters
    ----------
    adata: anndata object
        Object containing single cell RNA-seq data.
    group_column: string
        A column in adata.obs containing group labels.
    group_mutant: string
        Name of the first group.
    group_normal: string
        Name of the second group.
    layer: string
        Name of the adata layer to be used for calculation. Default is None. If default adata.X will be used for calculation.

    Returns
    -------
    adata: anndata object
        Original anndata object with two new added columns in adata.var. Columns correspond to 1) KS statistic number, 2) p-value. If the KS statistic is small or the p-value is high, then we cannot reject the null hypothesis in favor of the alternative.
    """
    if not layer:
        adata.var['ks-stat'] = 0
        adata.var['ks-pval'] = 1
    else:
        adata.var['ks-stat' + '_' + layer] = 0
        adata.var['ks-pval' + '_' + layer] = 1

    for gene in adata.var.index:
        d1 = adata[adata.obs[group_column] == group_mutant]
        d2 = adata[adata.obs[group_column] == group_normal]
        if not layer:
            d1 = d1.to_df()[gene]
            d2 = d2.to_df()[gene]
        else: 
            d1 = d1.to_df(layer = layer)[gene]
            d2 = d2.to_df(layer = layer)[gene]

        ks = ks_2samp(d1, d2)

        if not layer:
            adata.var.loc[gene, 'ks-stat'] = ks[0]
            adata.var.loc[gene, 'ks-pval'] = ks[1]
        else:
            adata.var.loc[gene, 'ks-stat' + '_' + layer] = ks[0]
            adata.var.loc[gene, 'ks-pval' + '_' + layer] = ks[1]

    return(adata)

# run when file is directly executed
if __name__ == '__main__':
    from .adata import dummy_anndata
    # create a dummy anndata object
    adata = dummy_anndata()
    adata = calc_ks_stats(adata, 'cell_type', 'Monocyte', 'B', 'log_transformed')
    print(adata.var)