from src.arkserver.lib import Ini
from src.arkserver.format.stream import Stream
import socket
import selectors
import types
from pathlib import Path


class GameBotServer:
    """
    Every Admin bot will be running this service
    """
    PATH = Path.cwd() / Path('config.ini')

    def __init__(self, host: str=None, port: str=None, timeout=5, config=None):
        ini = Ini(Path(config)) if config else Ini(self.PATH)
        self.host = host or ini['NETWORK']['host']
        self.port = port and int(port) or int(ini['NETWORK']['port'])
        self.selector = selectors.DefaultSelector()
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.settimeout(timeout)
        self.connected = False
        self.client_sockets = {}
        self.client_keys = {}

    def connect(self):
        self.lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.lsock.bind((self.host, self.port))
        self.lsock.listen()
        print(f"Listening on {self.host}:{self.port} (press CTRL-C to close server)")
        self.lsock.setblocking(False)
        self.selector.register(self.lsock, selectors.EVENT_READ, data=None)
        self.connected = True

    def disconnect(self):
        self.shutdown()
        self.selector.close()
        self.connected = False

    def accept_wrapper(self, key):
        sock = key.fileobj
        conn, (host, port) = sock.accept()  # Shoulbd be ready to read
        addr = f"{host}:{port}"
        print(f"Accepted connection from {addr}")

        self.client_sockets[addr] = sock
        self.client_keys[addr] = key

        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.selector.register(conn, events, data=data)

    def read(self, addr: str):
        sock = self.client_sockets[addr]
        fragments = bytearray()
        try:
            while True:
                chunk = bytearray(sock.recv(4096))  # Should be ready to read
                if not chunk:
                    break
                fragments += chunk
        except BlockingIOError:
            recv_data = bytes(fragments)
            stream = Stream(stream=recv_data)
            print(f'\033[93mReceived from client ({addr}): {stream.decode()}\033[0m')
            return recv_data

    def write(self, addr, data):
        stream = Stream.new(data)
        print(f'\033[93mSending to client ({addr}): {data}\033[0m')
        sock = self.client_sockets[addr]
        key = self.client_keys[addr]
        sent = sock.send(stream.encode())
        key.data.outb = key.data.outb[sent:]

    def disconnect_client(self, addr):
        print(f"Closing connection to {addr}")
        sock = self.client_sockets[addr]
        self.selector.unregister(sock)
        sock.close()
        del self.client_keys[addr]
        del self.client_sockets[addr]

    def shutdown(self):
        addresses = list(self.client_keys.keys())
        for addr in addresses:
            self.send_disconnect(addr)
            self.disconnect_client(addr)

    def send_disconnect(self, addr):
        sock = self.client_sockets[addr]
        data = self.client_keys[addr].data
        sent = sock.send("exit".encode())  # Should be ready to write
        data.outb = data.outb[sent:]

    def service_connection(self, key, mask):
        data = key.data
        addr = data.addr
        self.client_sockets[addr] = key.fileobj
        self.client_keys[addr] = key
        recv_data = None

        if mask & selectors.EVENT_READ:
            recv_data = self.read(addr)
            if recv_data:
                data.outb += recv_data
            else:
                self.disconnect_client(addr)
        if mask & selectors.EVENT_WRITE:
            if recv_data:
                stream = Stream(stream=recv_data)
                outgoing_data = {"success": f"{stream.decode()}"}
                self.write(addr, outgoing_data)  # Should be ready to write

    def run(self):
        self.connect()
        try:
            while True:
                events = self.selector.select(timeout=None)
                for selector_key, mask in events:
                    if selector_key.data is None:
                        self.accept_wrapper(selector_key)
                    else:
                        self.service_connection(selector_key, mask)
        except KeyboardInterrupt:
            print("\nCaught keyboard interrupt, exiting:")
        finally:
            self.disconnect()
            print(f"All connections closed.")

    def __repr__(self):
        attr = {
            'connected': self.connected,
            'host': self.host,
            'port': self.port
            }
        items = []
        for k, v in attr.items():
            items.append(f"\033[34m{k}\033[90m=\033[0m{repr(v)}\033[0m")
        args = ', '.join(items)
        return f'<\033[96mGameBotServer\033[0m({args})>\033[0m'


if __name__ == "__main__":
    class A:
        def __init__(self):
            self.a = 1

        def __getitem_(self, item):
            return self.__dict__[item]

        def keys(self):
            return self.__dict__.keys()

        def __str__(self):
            return f"<A(a={repr(self.a)})>"

        def __repr__(self):
            return f"<A(a={repr(self.a)})>"


if __name__ == "__main__":
    "s.bind(('', 80)) specifies that the socket is reachable by any address the machine happens to have"
    game_server = GameBotServer(host='')  # same as 0.0.0.0
    #game_server = GameBotServer(host='0.0.0.0')
    #game_server = GameBotServer(host='172.20.176.1')
    #game_server = GameBotServer(host='192.168.56.1')
    #game_server = GameBotServer(host='192.168.1.135')
    #game_server = GameBotServer(host=socket.gethostname())
    #game_server = GameBotServer(host=socket.gethostbyname(socket.gethostname()))
    game_server.run()

