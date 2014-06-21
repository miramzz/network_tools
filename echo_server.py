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
<<<<<<< HEAD
    buffsize = 4096
    my_msg = ''
=======
    buffsize = 32
>>>>>>> ab87bb52f3794b0f3bf6bd10c3ae2de95d830b43

    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.bind(address)
    my_socket.listen(1)
<<<<<<< HEAD
    while True:
        conn, client_add = my_socket.accept()
        while  True:
            recv_msg = conn.recv(buffsize)
            my_msg += recv_msg
            if (len(recv_msg) < buffsize):
                break
    conn.shutdown(socket.SHUT_RD)
    conn.sendall(my_msg)
    conn.shutdown(socket.SHUT_WR)
    conn.close()
    my_socket.close()

if __name__=="__main__":
    p = Process(target=echo_server)
    p.start()
    p.join()





=======
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
>>>>>>> ab87bb52f3794b0f3bf6bd10c3ae2de95d830b43
