from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from constants import SOCK_TYPE
from typing import Tuple


class SocketServer:
    def __init__(self, address, socket_type):
        self.address = address
        self.socket_type = socket_type
        self.socket = None

    def udp_listen(self):
        while 1:
            print('Waiting for UDP connection')
            data, address = self.socket.recvfrom(1024)
            print(f'Response from {address}: {data.decode()}')
            self.socket.sendto(f"Connected to server with UDP".encode(), address)

    def tcp_listen(self):
        self.socket.listen()
        while 1:
            print('Waiting for TCP connection')
            client, address = self.socket.accept()
            with client:
                print(f"Connected by: {address}")
                while True:
                    data = client.recv(1024)
                    if not data:
                        print(f"Connection with {address} is closed")
                        break
                    print(f"Response from {address}: {data.decode()}")
                    client.send(f'Connected to server with TCP'.encode())

    def listen(self):
        with socket(AF_INET, self.socket_type) as socket_inst:
            self.socket = socket_inst
            self.socket.bind(self.address)
            if self.socket_type == SOCK_DGRAM:
                self.udp_listen()
            elif self.socket_type == SOCK_STREAM:
                self.tcp_listen()


class SocketClient:
    def __init__(self, address:  Tuple[int, int], socket_type: int = SOCK_STREAM):
        self._socket_type = socket_type
        self._addr = address
        self._socket_instance: socket = None
        self._setup_sock_connection()

    def _setup_sock_connection(self):
        self._socket_instance = socket(AF_INET, self._socket_type)
        if self._socket_type == SOCK_STREAM:
            self._socket_instance.connect(self._addr)

    def sent_message(self, sock_message: str):
        if self._socket_type == SOCK_DGRAM:
            self._send_to_udp(sock_message.encode())
        elif self._socket_type == SOCK_STREAM:
            self._send_to_tcp(sock_message.encode())

    def _send_to_udp(self, sock_message: bytes):
        self._socket_instance.sendto(sock_message, self._addr)

    def _send_to_tcp(self, sock_message: bytes):
        self._socket_instance.send(sock_message)

    def recv_message(self):
        data = self._socket_instance.recv(1024)
        print(f"Received from {SOCK_TYPE[self._socket_type]}: {data.decode()}")
