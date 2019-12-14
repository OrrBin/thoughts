import socket


class Connection:
    """
    Connection object that can send data represented by bytes, and receive data in a specified length.
    Can be used as a context manager.
    The classmethod connect, creates a new connection object, that is connected to the specified address (host:port)
    """

    @classmethod
    def connect(cls, host, port):
        sock = socket.socket()
        sock.connect((host, port))
        return Connection(sock)

    def __init__(self, sock):
        self.sock = sock

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __repr__(self):
        sock = self.sock.getsockname()
        peer = self.sock.getpeername()
        sock_ip = sock[0]
        sock_port = sock[1]
        peer_ip = peer[0]
        peer_port = peer[1]
        return f'<Connection from {sock_ip}:{sock_port} to {peer_ip}:{peer_port}>'

    def send(self, data):
        self.sock.sendall(data)

    def receive(self, size):
        x = b''
        original_size = size
        while size > 0:
            tmp = self.sock.recv(size)
            if not tmp:
                raise Exception(f'Could not read {original_size} bytes from socket')
            size -= len(tmp)
            x += tmp
        return x

    def close(self):
        self.sock.close()
