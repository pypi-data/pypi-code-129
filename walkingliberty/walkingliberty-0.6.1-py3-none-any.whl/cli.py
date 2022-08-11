"""
WalkingLiberty CLI
"""

import argparse

import segno

import walkingliberty


def address(args: argparse.Namespace) -> None:
    WalkingLiberty = walkingliberty.WalkingLiberty(
        args.currency, args.wallet_mode, args.phrase
    )
    address = WalkingLiberty.address()
    if args.qr is True:
        segno.make(address).terminal()
    print(address)


def private_key(args: argparse.Namespace) -> None:
    """Display the private key"""
    WalkingLiberty = walkingliberty.WalkingLiberty(
        args.currency, args.wallet_mode, args.phrase
    )
    print(WalkingLiberty.private_key.to_wif())


def balance(args: argparse.Namespace) -> None:
    WalkingLiberty = walkingliberty.WalkingLiberty(
        args.currency, args.wallet_mode, args.phrase
    )
    print(WalkingLiberty.balance(args.unit))


def send(args: argparse.Namespace) -> None:
    WalkingLiberty = walkingliberty.WalkingLiberty(
        args.currency, args.wallet_mode, args.phrase
    )
    print(WalkingLiberty.send(args.address, args.satoshis, args.unit))


def pay(args: argparse.Namespace) -> None:
    WalkingLiberty = walkingliberty.WalkingLiberty(
        args.currency, args.wallet_mode, args.phrase
    )
    print(WalkingLiberty.pay(args.uri))


def sweep(args: argparse.Namespace) -> None:
    WalkingLiberty = walkingliberty.WalkingLiberty(
        args.currency, args.wallet_mode, args.phrase
    )
    print(WalkingLiberty.sweep(args.address))


def main() -> None:
    parser = argparse.ArgumentParser(description="WalkingLiberty CLI.")
    parser.add_argument(
        "--currency", help="Currency: btc, bch, or bsv", type=str.lower, default="btc"
    )
    parser.add_argument(
        "--wallet-mode",
        help="Wallet mode: deterministic-type1, wif, or address",
        default="deterministic-type1",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"WalkingLiberty {walkingliberty.__version__}",
    )

    subparser = parser.add_subparsers()
    address_subparser = subparser.add_parser(
        "address", help="Returns phrase's address."
    )
    address_subparser.set_defaults(func=address)
    address_subparser.add_argument("phrase", help="Deterministic phrase.")
    address_subparser.add_argument(
        "--qr", help="QR code", action="store_true", default=False
    )

    private_key_subparser = subparser.add_parser(
        "private-key", help="Returns private key."
    )
    private_key_subparser.set_defaults(func=private_key)
    private_key_subparser.add_argument("phrase", help="Deterministic phrase.")

    balance_subparser = subparser.add_parser(
        "balance", help="Returns phrase's balance."
    )
    balance_subparser.add_argument("--unit", help="As unit/currency", default="satoshi")
    balance_subparser.set_defaults(func=balance)
    balance_subparser.add_argument("phrase", help="Deterministic phrase.")

    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    send_subparser = subparser.add_parser(
        "send", help="Sends cryptocurrency.", formatter_class=formatter_class
    )
    send_subparser.set_defaults(func=send)
    help = "Deterministic phrase."
    send_subparser.add_argument("phrase", help=help)
    help = "Address to send to."
    send_subparser.add_argument("address", help=help)
    help = "Satoshis to send"
    send_subparser.add_argument("satoshis", help=help, type=int)
    help = "As unit/currency"
    send_subparser.add_argument("--unit", help=help, default="satoshi")

    pay_subparser = subparser.add_parser(
        "pay", help="Pay a URI.", formatter_class=formatter_class
    )
    pay_subparser.set_defaults(func=pay)
    pay_subparser.add_argument("phrase", help="Deterministic phrase.")
    pay_subparser.add_argument("uri", help="URI to pay.")

    sweep_subparser = subparser.add_parser("sweep", help="Sweeps all cryptocurrency.")
    help = "Deterministic phrase."
    sweep_subparser.add_argument("phrase", help=help)
    help = "Address to send to."
    sweep_subparser.add_argument("address", help=help)
    sweep_subparser.set_defaults(func=sweep)

    args = parser.parse_args()
    # This calls the function or wrapper function, depending on what we set
    # above.
    if "func" in args:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
