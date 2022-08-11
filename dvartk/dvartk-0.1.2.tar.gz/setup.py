# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dvartk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dvartk',
    'version': '0.1.2',
    'description': '',
    'long_description': '# dvartk (variant comparison toolkit)\n## Install\n```\npip install dvartk\n```\n\n## Philosophy\nBasically a package for comparing SNVs of maf files\n- in the future, SV, INDEL support, vcf support as well\n\n## Usage\n### Comparing SNVs\n```\nimport dvartk\n\n# set MAF paths\nmaf1_path = \'/path/to/maf1\'\nmaf2_path = \'/path/to/maf2\'\n\n# convert custom chrom, pos, ref, alt column names to "chrom", "pos", "ref", "alt"\nsnv_file_config = dvartk.parser.SnvFileConfig(\'Chromosome\', \'Start_Position\', \'Reference_Allele\', \'Tumor_Seq_Allele2\')\n\n# load and convert columns of MAF\nmaf1 = dvartk.load_and_convert_snv_maf_columns(maf1_path, snv_file_config)\nmaf2 = dvartk.load_and_convert_snv_maf_columns(maf2_path, snv_file_config)\n\n# get set counts (intersection, difference, ...) between maf1 and maf2\n# first make a SNV comparison instance\nsnv_cmp = SnvComparison(maf1, maf2)\nsnv_cmp.get_set_counts() # get A[maf1], B[maf2] counts\nsummary = snv_cmp.make_oneliner()\nprint(summary)\n```\n\n### Plot SNV trinucleotide spectra\n```\nimport dvartk\n\n# set a MAF path\nmaf_path = \'/path/to/maf\'\n\n# get counts per trinucleotide type\ncounts = dvartk.count_snvs(maf)\ndvartk.plot_snv_spectra(\n    counts,\n    \'plot title\',  # title of the plot e.g. sample ID\n    save_path=None,  # output path for your plot; if None, don\'t save plot\n    tag=\' (bar)\'  # tag to add to plot title; if None, don\'t add tag\n)\n```\n',
    'author': 'Seongmin Choi',
    'author_email': 'soymintc@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
