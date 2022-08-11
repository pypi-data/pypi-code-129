from decimal import Decimal
from typing import Literal, Tuple


def decode_uri(currency: Literal["btc", "bch", "bsv"], uri: str) -> Tuple[str, int]:
    """
    decode_uri: Converts URI to address and Satoshis, validates against
    currency.

    amount is called amount because we may add a currency that doesn't have
    'satoshis' one day. This is meant to be normalizing.

    This does *not* validate address.
    """
    if "&" in uri:
        raise ValueError("& in URI not supported.")

    uri_currency = uri.split(":")[0]
    uri_address = uri.split(":")[1].split("?")[0]
    uri_amount = Decimal(uri.split("=")[1])

    address = uri_address
    satoshis = int(uri_amount * 100000000)

    if currency == "btc":
        if uri_currency != "bitcoin":
            raise ValueError("URI does not start with bitcoin: for BTC")
    elif currency == "bch":
        if uri_currency != "bitcoincash":
            raise ValueError("URI does not start with bitcoincash: for BCH")
        else:
            address = uri.split("?")[0]
    elif currency == "bsv":
        if uri_currency != "bitcoin":
            raise ValueError("URI does not start with bitcoin: for BSV")
    else:
        raise ValueError("Currency must be one of: btc, bch, bsv")

    return (address, satoshis)
