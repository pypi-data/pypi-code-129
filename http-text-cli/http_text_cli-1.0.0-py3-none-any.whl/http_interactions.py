import os, sys
from pathlib import Path
import logging

import requests
import json


def get_base_url(host, port):
    return f"http://{host}:{port}"


def do_request_response(base_url=None, host="localhost", port=3001, root_directory=None) -> None:
    """
    Do one http request and response. Parameters, urls etc are specified in files found in the current working directory (or root_directory if specified)

    Expects to find at least this file:

        * request_url.txt

    You may also specify files for headers, cookies, payload, in these files respectively:

        * request_headers.txt
        * request_cookies.txt
        * request_body.json

    It writes the response into files also in the current working directory (or root_directory if specified)

        * status_code.txt - HTTP status code
        * response_headers.txt - headers
        * response_cookies.txt - cookies
        * response_body.json or response_body.txt - payload

    :param base_url: the stem of the url eg http://localhost:3001
    :param host: instead of specifying a base_url you can specify host, http:// will be added to it, default is 'localhost'
    :param port: instead of specifying a base_url you can specify host and port, default is 3001
    :param root_directory: where to find the files specifying the http request, default is current working directory
    """
    base_url = base_url or get_base_url(host, port)
    root_directory = root_directory or Path(os.getcwd())

    request = read_http_parameters(base_url, root_directory)
    response = request.do_http()
    write_response_files(response, root_directory)


class HttpRequest:
    def __init__(self, url, method, headers, cookies, payload):
        self.url = url
        self.method = method
        self.headers = headers
        self.cookies = cookies
        self.payload = payload

    def do_http(self) -> requests.Response:
        if "GET" in self.method:
            r = self.do_get()
        elif "POST" in self.method:
            r = self.do_post()
        elif "PUT" in self.method:
            r = self.do_put()
        elif "PATCH" in self.method:
            r = self.do_patch()
        elif "DELETE" in self.method:
            r = self.do_delete()
        else:
            raise RuntimeError(f"bad http method: {self.method}")
        return r

    def do_get(self):
        return requests.get(self.url, headers=self.headers, cookies=self.cookies)

    def do_post(self):
        return requests.post(self.url, json=self.payload, headers=self.headers, cookies=self.cookies)

    def do_put(self):
        return requests.put(self.url, json=self.payload, headers=self.headers, cookies=self.cookies)

    def do_patch(self):
        return requests.patch(self.url, json=self.payload, headers=self.headers, cookies=self.cookies)

    def do_delete(self):
        return requests.delete(self.url, json=self.payload, headers=self.headers, cookies=self.cookies)


def read_payload_file(filename: Path):
    if not filename.exists():
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def read_http_config_file(filename: Path):
    if not filename.exists():
        raise ValueError(f"filename does not exist: {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        method, url = f.read().split()
        method = method.upper()
        logging.info(f"found http method {method} for url {url}")
        return method, url


def read_key_value_file(filename: Path):
    the_dict = {}
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            for line in f:
                key, value = line.split(":")
                the_dict[key.strip()] = value.strip()
    return the_dict


def write_key_value(the_dict, filename):
    if not the_dict:
        return
    with open(filename, "w") as f:
        for header, value in sorted(the_dict.items()):
            f.write(f"{header}: {value}\n")


def read_http_parameters(base_url, root_directory: Path) -> HttpRequest:
    method, url = read_http_config_file(root_directory / "request_url.txt")

    return HttpRequest(
        url=f"{base_url}{url}",
        method=method,
        headers=read_key_value_file(root_directory / "request_headers.txt"),
        cookies=read_key_value_file(root_directory / "request_cookies.txt"),
        payload=read_payload_file(root_directory / "request_body.json"),
    )


def is_json(response: requests.Response):
    return "json" in response.headers["Content-Type"]


def write_response_files(response: requests.Response, root_directory: Path):
    with open(root_directory / "response_status_code.txt", "w") as f:
        f.write(str(response.status_code))

    if is_json(response):
        with open("response_body.json", "w") as f:
            f.write(response.text)
    else:
        with open("response_body.txt", "w") as f:
            f.write(response.text)

    write_key_value(response.headers, "response_headers.txt")
    write_key_value(response.cookies, "response_cookies.txt")
