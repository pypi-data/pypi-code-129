'''Metadata about uniprot data sources.'''

# List of known data sets in Uniprot.
UNIPROT_DATASETS = ['uniprotkb', 'uniref', 'uniparc', 'proteomes',
                  'taxonomy', 'keywords', 'citations', 'diseases',
                  'database', 'locations', 'unirule', 'arba']

# Dict of data formats available for different data sets.
valid_data_formats = {
    'uniprotkb': ['fasta', 'tsv', 'xlsx', 'json', 'xml', 'rdf', 'txt', 'gff', 'list'],
    'uniref': ['fasta', 'tsv', 'xlsx', 'json', 'list'],
    'uniparc': ['fasta', 'tsv', 'xlsx', 'json', 'xml', 'rdf', 'list'],
    'proteomes': ['tsv', 'xlsx', 'json', 'xml', 'rdf', 'list'],
    'taxonomy': ['tsv', 'xlsx', 'json', 'list'],
    'keywords': ['tsv', 'xlsx', 'json', 'list', 'obo'],
    'citations': ['tsv', 'xlsx', 'json', 'list'],
    'diseases': ['tsv', 'xlsx', 'json', 'list', 'obo'],
    'database': ['json'],
    'locations': ['tsv', 'xlsx', 'json', 'list', 'obo'],
    'unirule': ['json', 'list'],
    'arba': ['json', 'list'],
}


def is_format_valid(dataset: str, data_format: str):
    '''Checks whether a data format is available for the desired data set.'''
    return data_format in valid_data_formats[dataset]
