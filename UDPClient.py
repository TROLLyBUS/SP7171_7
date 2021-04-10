from os import getenv
from socket import SOCK_DGRAM
from SocketManager import SocketClient
from constants import SOCK_TYPE

if __name__ == '__main__':
    client_sock_type = SOCK_DGRAM
    address = (getenv("SOCK_SERVER_HOST", "localhost"),
               int(getenv("SOCK_SERVER_PORT", 51312)))
    client = SocketClient(address, client_sock_type)
    client.sent_message(f"Client is connected with "
                        f"{SOCK_TYPE[client_sock_type]} connection")
    client.recv_message()

