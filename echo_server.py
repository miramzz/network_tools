#!/usr/bin/env python
import socket
import sys


def echo_server():
    try:
        my_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP
            )
    except socket.error:
        print u"Failed to create socket"
        sys.exit()

    address = ('127.0.0.1', 5000)
    buffsize = 32

    my_socket.bind(address)
    my_socket.listen(1)
    try:
        while True:
            conn, client_add = my_socket.accept()
            my_msg = ''
            while True:
                recv_msg = conn.recv(buffsize)
                my_msg += recv_msg
                if (len(recv_msg) < buffsize):
                    print recv_msg
                    break
            conn.shutdown(socket.SHUT_RD)
            conn.sendall(my_msg)
            conn.shutdown(socket.SHUT_WR)
            conn.close()
    except KeyboardInterrupt:
        my_socket.close()

if __name__ == "__main__":
    echo_server()
