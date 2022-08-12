#!/usr/bin/env python3

from __future__ import annotations
import requests

# GET one object
def rget(key: str, host: str = "localhost", port: int = 8080, db: int = 0) -> any:
    return rsend("get", host, port, db, key)

# POST one object
def rset(key: str, value: str, host: str = "localhost", port: int = 8080, db: int = 0):
    return rsend("set", host, port, db, key, value)

# GET all keys
def rkeys(host: str = "localhost", port: int = 8080, db: int = 0) -> list[str]:
    return rsend("get", host, port, db)

# Send a request
def rsend(method: str, key: str, value: str, host: str = "localhost", port: int = 8080, db: int = 0):
    params = {}
    if key != "":
        params.update({"key": key})
    if value != "":
        params.update({"value": value})
    resp = requests.get(f"http://{host}:{port}/{db}/{method}", params=params)
    return resp.json()
