
import socket
import logging
import os
from subprocess import Popen, PIPE
import time


def find_available_ports(portcount=1):
    """Returns a number of ports that are available for a Python process to bind to"""
    result = []
    socks = []
    for i in range(portcount):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 0))
        s.listen(1)
        socks.append(s)
        result.append(s.getsockname()[1])

    for sock in socks:
        sock.close()

    return result


def find_unique_port(unique_string=None, minimum_port=3001):
    """Returns a port that is:
        - greater than or equal to the minimum_port given
        - uses a hash of the unique_string argument. If this is None then it uses the TEXTTEST_SANDBOX environment variable which should be unique for the currently executing test
    """
    unique_string = unique_string or os.environ.get("TEXTTEST_SANDBOX")
    if unique_string is None:
        return str(minimum_port)
    port = abs(hash(unique_string)) % (65536 - minimum_port)
    port += minimum_port
    return port


def start_server(command: list, port: int, ready_message=None, retry_count=3, additional_environment=None):
    logging.info("starting server")
    cwd = os.getcwd()
    my_env = os.environ.copy()
    if additional_environment:
        for key, value in additional_environment.items():
            my_env[key] = value

    my_env["PORT"] = f"{port}"

    p = Popen(command,
              shell=True,
              cwd=cwd,
              stdout=PIPE,
              env=my_env)

    # Wait for the server to emit the specified 'ready message'
    if ready_message:
        count = 0
        while count < retry_count:
            msg = p.stdout.readline()
            if ready_message in msg:
                time.sleep(0.05)
                break
            else:
                logging.info(f"server: {msg}")
            count += 1
    return p


def stop_server(process):
    logging.info("stopping server")
    process.terminate()
