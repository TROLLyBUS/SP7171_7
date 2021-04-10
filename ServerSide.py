from socket import SOCK_STREAM, SOCK_DGRAM
from SocketManager import SocketServer
import threading

if __name__ == '__main__':
    tcp = SocketServer(('localhost', 54514), SOCK_STREAM)
    tcp = threading.Thread(target=tcp.listen)
    udp = SocketServer(('localhost', 51312), SOCK_DGRAM)
    udp = threading.Thread(target=udp.listen)
    tcp.start()
    udp.start()


