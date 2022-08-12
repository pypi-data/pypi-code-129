'''Dispatcher for cli arguments.'''

import sys
import argparse

from .writer import fetch_and_save, fetch_and_print


VERSION = 'v0.3.4'


def cli_input(text: str, def_val=None, y_or_n=False):
    '''Prompts the user for input with default value.'''
    try:
        from_user = input(text)

        if y_or_n:
            if from_user.strip().lower() == 'y':
                return True
            if from_user.strip().lower() == 'n':
                return False

            print("WARNING - Unrecognizable input. Using default value.")
            return def_val

        if def_val:
            return from_user if from_user != '' else def_val

        return from_user
    except (KeyboardInterrupt, EOFError):
        print('\nSearch cancelled.')
        sys.exit(0)


def get_parser():
    '''Constructs and returns an ArgumentParser.'''
    parser = argparse.ArgumentParser(
        prog='uniprot-cli',
        description='The Unofficial Uniprot client.')
    parser.add_argument('-q', '--query', dest='query', type=str)
    parser.add_argument('-m', '--multiple', dest='multiple', type=bool, default=False)
    parser.add_argument('-f', '--format', dest='data_format', type=str, default='fasta')
    parser.add_argument('-d', '--dataset', dest='dataset', type=str, default='uniprotkb')
    parser.add_argument('-n', '--nosave', dest='nosave', action='store_true')
    parser.add_argument('-v', '--version', action='version', version=f"%(prog)s {VERSION}")

    return parser


def dispatch_and_run():
    '''Dispatches flow to handlers based on passed arguments.'''
    parser = get_parser()
    args = parser.parse_args()

    if args.query is None:
        print(f"uniprot-cli - {VERSION}")
        query = cli_input('Enter uniprot query: ')

        data_format = cli_input(
            f"Enter data format (default: '{args.data_format}'): ",
            args.data_format)

        dataset = cli_input(
            f"Enter data set (default: '{args.dataset}'): ",
            args.dataset)

        nosave = cli_input(
            "Save the result to file [Y/n]: ",
            True,
            y_or_n=True)

        if not nosave:
            fetch_and_print(
                query=query,
                data_format=args.data_format,
                dataset=args.dataset)
        else:
            fetch_and_save(
                query=query,
                data_format=data_format,
                dataset=dataset)
    else:
        if args.nosave:
            fetch_and_print(
                query=args.query,
                data_format=args.data_format,
                dataset=args.dataset)
        else:
            fetch_and_save(
                query=args.query,
                data_format=args.data_format,
                dataset=args.dataset)
