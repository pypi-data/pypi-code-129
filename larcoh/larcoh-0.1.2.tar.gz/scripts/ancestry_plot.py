#!/usr/bin/env python

"""
Plot ancestry PCA analysis results
"""

import logging
from collections import Counter
from typing import List, Iterable, Optional

import click
import pandas as pd
import numpy as np
import hail as hl
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.transform import factor_cmap, factor_mark
from bokeh.plotting import ColumnDataSource, figure
from bokeh.palettes import turbo  # flake: disable=F401
from bokeh.models import CategoricalColorMapper, HoverTool

from joint_calling import utils, resources
from joint_calling import _version


logger = logging.getLogger(__file__)
logging.basicConfig(format='%(levelname)s (%(name)s %(lineno)s): %(message)s')
logger.setLevel(logging.INFO)


@click.command()
@click.version_option(_version.__version__)
@click.option(
    '--meta-tsv',
    'meta_tsv_path',
    callback=utils.get_validation_callback(ext='tsv', must_exist=True),
    required=True,
)
@click.option(
    '--eigenvalues-ht',
    'eigenvalues_ht_path',
    required=True,
    callback=utils.get_validation_callback(ext='ht', must_exist=True),
)
@click.option(
    '--scores-ht',
    'scores_ht_path',
    required=True,
    callback=utils.get_validation_callback(ext='ht', must_exist=True),
)
@click.option(
    '--loadings-ht',
    'loadings_ht_path',
    required=True,
    callback=utils.get_validation_callback(ext='ht', must_exist=True),
)
@click.option(
    '--inferred-pop-ht',
    'inferred_pop_ht_path',
    required=True,
    callback=utils.get_validation_callback(ext='ht', must_exist=True),
)
@click.option('--out-path-pattern', 'out_path_pattern')
@click.option(
    '--hail-billing',
    'hail_billing',
    required=True,
    help='Hail billing account ID.',
)
def main(  # pylint: disable=too-many-arguments,too-many-locals,missing-function-docstring
    meta_tsv_path: str,
    eigenvalues_ht_path: str,
    scores_ht_path: str,
    loadings_ht_path: str,
    inferred_pop_ht_path: str,
    out_path_pattern: Optional[str],
    hail_billing: str,  # pylint: disable=unused-argument
):
    local_tmp_dir = utils.init_hail(__file__)

    meta_ht = utils.parse_input_metadata(meta_tsv_path, local_tmp_dir)

    produce_plots(
        eigenvalues_ht_path=eigenvalues_ht_path,
        scores_ht_path=scores_ht_path,
        loadings_ht_path=loadings_ht_path,
        inferred_pop_ht_path=inferred_pop_ht_path,
        meta_ht=meta_ht,
        out_path_pattern=out_path_pattern,
    )


def summarize_projects_by_pop(ht):
    """
    Make labels that split samples for a population by project
    """
    cnts_by_pop = dict()
    data = ht.select('pop', 'project').collect()
    for d in data:
        if d.pop not in cnts_by_pop:
            cnts_by_pop[d.pop] = dict()
        if d.project not in cnts_by_pop[d.pop]:
            cnts_by_pop[d.pop][d.project] = 0
        cnts_by_pop[d.pop][d.project] += 1
    
    summary_by_pop = {
        pop: ', '.join(f'{project}: {cnt}' for project, cnt in sorted(proj_d.items())) 
        for pop, proj_d in cnts_by_pop.items()
    }
    summary_by_pop = {k: v for k, v in summary_by_pop.items() if k}
    summary_by_pop = hl.literal(summary_by_pop)
    return summary_by_pop


BG_LABEL = 'Provided ancestry (1KG+HGDP)'
FG_LABEL = 'Inferred ancestry'


def produce_plots(
    eigenvalues_ht_path: str,
    scores_ht_path: str,
    loadings_ht_path: str,
    inferred_pop_ht_path: str,
    meta_ht: hl.Table,
    out_path_pattern: Optional[str] = None,
    number_of_pcs: Optional[int] = None,
):
    """
    Generate plots in HTML format, write for each PC (of n_pcs) and
    scope ("project", "population") plus for loadings) into
    file paths defined by `out_path_pattern`.
    """
    scores_ht = hl.read_table(scores_ht_path)
    inferred_pop_ht = hl.read_table(inferred_pop_ht_path)

    scores_ht = scores_ht.annotate(
        pop=inferred_pop_ht[scores_ht.s].pop,
        is_training=inferred_pop_ht[scores_ht.s].is_training,
        project=meta_ht[scores_ht.s].project
    ).cache()

    def key_by_external_id(ht, meta_ht=None):
        """
        Assuming ht.s is a CPG id, replaces it with external ID, 
        assuming it's defined in meta_ht.external_id
        """
        if meta_ht is None:
            meta_ht = ht
        ht = ht.annotate(old_s=ht.s).key_by('old_s')
        ht = (
            ht.annotate(
                s=hl.if_else(
                    hl.is_defined(meta_ht[ht.old_s]),
                    meta_ht[ht.old_s].external_id,
                    ht.old_s,
                )
            )
            .key_by('s')
            .drop('old_s')
        )
        return ht
    
    ht = key_by_external_id(scores_ht, meta_ht)

    pop_full_names = hl.literal({
        'nfe': 'Non-Finnish European', 
        'fin': 'Finnish',
        'mid': 'Middle Eastern',
        'oth': 'Other',
        'afr': 'African/African American',
        'eas': 'East Asian',
        'sas': 'South Asian',
        'amr': 'Latino/Admixed American',
    })
    ht = ht.annotate(pop=pop_full_names[ht.pop])
    ht = ht.cache()

    eigenvalues = hl.read_table(eigenvalues_ht_path).f0.collect()
    eigenvalues_df = pd.to_numeric(eigenvalues)
    variance = np.divide(eigenvalues_df[1:], float(eigenvalues_df.sum())) * 100
    variance = variance.round(2)
    number_of_pcs = number_of_pcs or len(eigenvalues_df) - 1

    plots = []

    sample_names = ht.s.collect()
    projects = ht.project.collect()
    is_training = ht.is_training.collect()
    
    for scope, title, labels in [
        ('project', 'Project', projects),
        ('population', 'Population', ht.pop.collect()),
    ]:
        plots.extend(
            _plot_pca(
                scope=scope,
                title=title,
                labels=labels,
                number_of_pcs=number_of_pcs,
                variance=variance,
                ht=ht,
                projects=projects,
                is_training=is_training,
                sample_names=sample_names,
                out_path_pattern=out_path_pattern,
            )
        )

    plots.extend(
        _plot_loadings(
            number_of_pcs, loadings_ht_path, out_path_pattern=out_path_pattern
        )
    )

    return plots


def _plot_pca(
    scope,
    title,
    labels,
    number_of_pcs,
    variance,
    ht,
    projects,
    sample_names,
    is_training,
    out_path_pattern=None,
):
    
    cntr: Counter = Counter(labels)
    labels = [f'{x} ({cntr[x]})' for x in labels]

    unique_labels = list(Counter(labels).keys())
    tooltips = [('labels', '@label'), ('samples', '@samples')]
    plots = []
    for i in range(number_of_pcs - 1):
        pc1 = i
        pc2 = i + 1
        plot = figure(
            title=title,
            x_axis_label=f'PC{pc1 + 1} ({variance[pc1]})%)',
            y_axis_label=f'PC{pc2 + 1} ({variance[pc2]}%)',
            tooltips=tooltips,
            width=1000,
        )
        source = ColumnDataSource(
            dict(
                x=ht.scores[pc1].collect(),
                y=ht.scores[pc2].collect(),
                label=labels,
                samples=sample_names,
                project=projects,
                is_training=[
                    {True: BG_LABEL, False: FG_LABEL}.get(v) 
                    for v in is_training
                ],
            )
        )
        plot.scatter(
            'x',
            'y',
            alpha=0.5,
            marker=factor_mark('is_training', ['cross', 'circle'], [BG_LABEL, FG_LABEL]),
            source=source,
            size=4,
            color=factor_cmap('label', ['#1b9e77', '#d95f02'], unique_labels),
            legend_group='label',
        )
        plot.add_layout(plot.legend[0], 'left')
        plots.append(plot)
        if out_path_pattern:
            html = file_html(plot, CDN, title)
            plot_filename_html = out_path_pattern.format(
                scope=scope, pci=pc2, ext='html'
            )
            with hl.hadoop_open(plot_filename_html, 'w') as f:
                f.write(html)
    return plots


def _plot_loadings(number_of_pcs, loadings_ht_path, out_path_pattern=None):
    loadings_ht = hl.read_table(loadings_ht_path)
    plots = []
    gtf_ht = hl.experimental.import_gtf(
        resources.GENCODE_GTF,
        reference_genome='GRCh38',
        skip_invalid_contigs=True,
        min_partitions=12,
        force_bgz=True,
    )
    for i in range(number_of_pcs - 1):
        pc = i + 1
        plot = manhattan_loadings(
            iteration=i,
            gtf=gtf_ht,
            loadings=loadings_ht,
            title='Loadings of PC ' + str(pc),
            collect_all=True,
        )
        plots.append(plot)
        if out_path_pattern:
            html = file_html(plot, CDN, 'my plot')
            plot_filename_html = out_path_pattern.format(
                scope='loadings', pci=pc, ext='html'
            )
            with hl.hadoop_open(plot_filename_html, 'w') as f:
                f.write(html)
    return plots


def manhattan_loadings(
    iteration,
    gtf,
    loadings,
    title=None,
    size=4,
    hover_fields=None,
    collect_all=False,
    n_divisions=500,
):
    """modify hail manhattan plot"""
    palette = [
        '#1f77b4',
        '#ff7f0e',
        '#2ca02c',
        '#d62728',
        '#9467bd',
        '#8c564b',
        '#e377c2',
        '#7f7f7f',
        '#bcbd22',
        '#17becf',
    ]

    # add gene names, p-values, and locus info
    loadings = loadings.annotate(gene_names=gtf[loadings.locus].gene_name)
    pvals = hl.abs(loadings.loadings[iteration])
    locus = loadings.locus

    if hover_fields is None:
        hover_fields = {}

    hover_fields['locus'] = hl.str(locus)
    hover_fields['gene'] = hl.str(loadings.gene_names)

    source_pd = (
        hl.plot.plots._collect_scatter_plot_data(  # pylint: disable=protected-access
            ('_global_locus', locus.global_position()),
            ('_pval', pvals),
            fields=hover_fields,
            n_divisions=None if collect_all else n_divisions,
        )
    )
    source_pd['p_value'] = source_pd['_pval']
    source_pd['_contig'] = [locus.split(':')[0] for locus in source_pd['locus']]

    observed_contigs = set(source_pd['_contig'])
    ref = locus.dtype.reference_genome
    observed_contigs = [
        contig for contig in ref.contigs.copy() if contig in observed_contigs
    ]

    contig_ticks = [
        ref._contig_global_position(contig)  # pylint: disable=protected-access
        + ref.contig_length(contig) // 2
        for contig in observed_contigs
    ]
    color_mapper = CategoricalColorMapper(
        factors=ref.contigs, palette=palette[:2] * int((len(ref.contigs) + 1) / 2)
    )

    p = figure(
        title=title, x_axis_label='Chromosome', y_axis_label='Loadings', width=1000
    )
    (
        p,
        _,
        legend,
        _,
        _,
        _,
    ) = hl.plot.plots._get_scatter_plot_elements(  # pylint: disable=protected-access
        p,
        source_pd,
        x_col='_global_locus',
        y_col='_pval',
        label_cols=['_contig'],
        colors={'_contig': color_mapper},
        size=size,
    )
    legend.visible = False
    p.xaxis.ticker = contig_ticks
    p.xaxis.major_label_overrides = dict(zip(contig_ticks, observed_contigs))
    p.select_one(HoverTool).tooltips = [
        t for t in p.select_one(HoverTool).tooltips if not t[0].startswith('_')
    ]

    return p


def remove_duplicates(x: Iterable) -> List:
    """
    Removes duplicates from a list, keeps order
    """
    return list(dict.fromkeys(x))


if __name__ == '__main__':
    main()  # pylint: disable=E1120
