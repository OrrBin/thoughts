from .connection import Connection
import socket


class Listener:
    """
    Listener service which listens to new connections on the specified address (host:port)
    Returning new Connection object for each incoming connection.
    Can be used as a context manager
    """

    def __init__(self, port, host='0.0.0.0', backlog=1000, reuse_address=True):
        self.port = port
        self.host = host
        self.backlog = backlog
        self.reuse_address = reuse_address
        self.server = socket.socket()

    def __repr__(self):
        port_r = f'port={self.port!r}'
        host_r = f'host={self.host!r}'
        backlog_r = f'backlog={self.backlog!r}'
        reuse_address_r = f'reuse_address={self.reuse_address!r}'
        return f'Listener({port_r}, {host_r}, {backlog_r}, {reuse_address_r})'

    def start(self):
        if self.reuse_address:
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.bind((self.host, self.port))
        self.server.listen(self.backlog)

    def stop(self):
        self.server.close()

    def accept(self):
        client_socket, address = self.server.accept()
        return Connection(client_socket)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
