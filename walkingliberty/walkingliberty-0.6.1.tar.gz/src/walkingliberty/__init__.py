"""
WalkingLiberty

Sort of a Bitcoin, Bitcoin Cash, and Bitcoin SV wallet API
"""

from hashlib import sha256
from importlib.metadata import version
from typing import Literal, Optional, Union

import bit
import bitcash
import bitsv

from walkingliberty.utilities import decode_uri

__version__ = version(__package__)

VALID_CURRENCIES = ("btc", "bch", "bsv")
VALID_WALLET_MODES = ("deterministic-type1", "wif", "address")


class WalkingLiberty:
    """
    WalkingLiberty class.

    private_key is address when wallet_mode is set to address.
    """

    def __init__(
        self,
        currency: Literal["btc", "bch", "bsv"],
        wallet_mode: Literal["deterministic-type1", "wif", "address"],
        private_key: str,
    ) -> None:
        if currency not in VALID_CURRENCIES:
            message = "currency must be one of: {}".format(VALID_CURRENCIES)
            raise ValueError(message)

        if wallet_mode not in VALID_WALLET_MODES:
            message = "wallet_mode must be one of: {}".format(VALID_WALLET_MODES)
            raise ValueError(message)

        if currency == "btc":
            self.bit = bit
        elif currency == "bch":
            self.bit = bitcash
        elif currency == "bsv":
            self.bit = bitsv

        self.currency = currency
        self.wallet_mode: str = wallet_mode
        self._satoshis: Optional[int] = None

        if self.wallet_mode == "deterministic-type1":
            private_key_bytes = bytes(private_key, "utf-8")
            self.private_key = self.bit.Key.from_hex(
                sha256(private_key_bytes).hexdigest()
            )
        elif self.wallet_mode == "wif":
            self.private_key = self.bit.Key(private_key)

        if self.wallet_mode == "address":
            self._address = private_key
        else:
            address = self.private_key.address
            assert isinstance(address, str), "address must be string"
            self._address = address

    def address(self) -> str:
        """
        Returns address for key
        """
        return self._address

    def balance(
        self, unit: str = "satoshi", use_cache: bool = False
    ) -> Union[int, str]:
        """
        Returns balance for a private key's address.

        Optionally, set unit for desired unit. (satoshi, btc, bsv, usd, etc)

        use_cache: Controls whether we cache the balance or not.

        Let's say you wanted to get balance in satoshis and USD,
        this would be only query the Blockchain APIs once. But, if
        you want to monitor balance over time on the same WalkingLiberty
        object, the cache would get the starting balance, only.
        """
        if self.currency == "bsv":
            NetworkAPI = self.bit.network.NetworkAPI("main")
        else:
            NetworkAPI = self.bit.network.NetworkAPI

        if use_cache:
            if self._satoshis is None:
                self._satoshis = NetworkAPI.get_balance(self._address)

            satoshis = self._satoshis
        else:
            satoshis = NetworkAPI.get_balance(self._address)

        satoshi_to_currency = self.bit.network.satoshi_to_currency_cached
        balance = satoshi_to_currency(satoshis, unit)

        # Return int if satoshis, str if anything else.
        if unit == "satoshi":
            return int(balance)
        else:
            assert isinstance(balance, str), "balance must be str."
            return balance

    def send(self, address: str, satoshis: int, unit: str = "satoshi") -> str:
        """
        Sends amount to address from the private_key's wallet.

        Returns TXID.
        """
        if self.wallet_mode == "address":
            raise ValueError("Cannot send without private key.")

        outputs = [(address, satoshis, unit)]
        # Have to call get_unspents() or get_balance() before send()
        self.private_key.get_unspents()
        txid = self.private_key.send(outputs, combine=False)
        assert isinstance(txid, str), "TXID must be str."
        return txid

    def pay(self, uri: str) -> str:
        """
        Pays URI.

        Returns TXID.
        """
        if self.wallet_mode == "address":
            raise ValueError("Cannot pay without private key.")

        address, satoshis = decode_uri(self.currency, uri)
        outputs = [(address, satoshis, "satoshi")]
        # Have to call get_unspents() or get_balance() before send()
        self.private_key.get_unspents()
        txid = self.private_key.send(outputs, combine=False)
        assert isinstance(txid, str), "TXID must be str."
        return txid

    def sweep(self, address: str) -> str:
        """
        Sweeps all coins from private_key into address.

        Returns TXID.
        """
        if self.wallet_mode == "address":
            raise ValueError("Cannot sweep without private key.")

        self.private_key.get_unspents()
        txid = self.private_key.send([], combine=True, leftover=address)
        assert isinstance(txid, str), "TXID must be str."
        return txid
