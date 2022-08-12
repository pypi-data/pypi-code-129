'''Functionality for fetching individual proteins in various formats.'''

import sys
import requests

from .datasources import UNIPROT_DATASETS, is_format_valid

UNIPROT_URL = 'http://uniprot.org/uniprot/'

BASE_API_URL = 'https://rest.uniprot.org/'


class EntryNotFoundException(BaseException):
    '''Exception for cases where a protein does not exist on uniprot.'''


class UnknownDataSetError(BaseException):
    '''Exception for when trying to query from an invalid data set.'''


class UnsupportedDataFormatError(BaseException):
    '''
    Exception for cases where the user tries to query a data set
    with an unsupported format.
    '''


def format_url(query: str, data_format='fasta', dataset='uniprotkb'):
    '''Formats a URL for uniprot REST API.'''
    if dataset in UNIPROT_DATASETS:
        return BASE_API_URL + dataset + '/' + query + '.' + data_format

    raise UnknownDataSetError()


def fetch(query: str, data_format='fasta', dataset='uniprotkb'):
    '''Downloads the protein sequence from uniprot as a .fasta file.'''
    try:
        if not is_format_valid(dataset, data_format):
            raise UnsupportedDataFormatError()

        url = format_url(query, data_format, dataset)
    except UnknownDataSetError:
        print(f"Error - Data set: {dataset} is unknown to uniprot.")
        sys.exit(-1)
    except UnsupportedDataFormatError:
        print(f"Error - Format '.{data_format}' is not supported for {dataset}.")
        sys.exit(-1)
    response = requests.get(url)

    if response.status_code != 200:
        raise EntryNotFoundException()

    return response.content.decode()
