"""pynetsys is a collection of tools and malicious packets."""

from .constants import Protocol, Packets
from . import _tool, _packet
from requests import get
from socket import getfqdn

__version__ = []

tool, packet = _tool, _packet

def isOnline(Address: str):
    # IMPORT
    from scapy.layers.inet import IP

    # RUN & RETURN
    if get(getfqdn(Address)).status_code == 200:
        return True
    else:
        return False
