import re
import sys
from pathlib import PurePosixPath

import configargparse
import hvac


def parse_args():
    parser = configargparse.ArgumentParser(
        add_env_var_help=True,
        auto_env_var_prefix='VAULT_',
    )
    parser.add_argument('--addr', help='Vault address', required=True)
    parser.add_argument('--token', help='Vault token', required=True)
    parser.add_argument('--namespace', help='Vault namespace', default=None)
    parser.add_argument('--pattern', help='Pattern to search for', default=r'''vault:([^\s'"]+)''')
    parser.add_argument('--prefix', help='Common vault key prefix', default='')
    parser.add_argument('files', help='Files to decrypt or \'-\' to read from stdin', nargs='+')

    return parser.parse_args()


def main():
    args = parse_args()

    client = hvac.Client(url=args.addr, token=args.token, namespace=args.namespace)

    for file_name in args.files:
        if file_name != '-':
            with open(file_name, 'r', encoding='utf8') as f_in:
                data = f_in.read()
        else:
            data = sys.stdin.read()

        for match in re.finditer(
            pattern=args.pattern,
            string=data,
        ):
            substr = match.group(0)
            key = match.group(1)
            if args.prefix and not key.startswith('/'):
                key = str(PurePosixPath('/') / args.prefix / key)

            _, mount_point, path = key.split('/', maxsplit=2)

            value = client.secrets.kv.v2.read_secret_version(path=path, mount_point=mount_point)
            value = value.get('data', {}).get('data', {}).get('value')
            assert value is not None, f'Value for key "{key}| is not set'

            data = data.replace(substr, value)

            print(f'Replaced "{key}" value', file=sys.stderr)

        if file_name != '-':
            with open(file_name, 'w', encoding='utf8') as f_out:
                f_out.write(data)
        else:
            sys.stdout.write(data)


if __name__ == '__main__':
    sys.exit(main())
