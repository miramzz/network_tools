#!/usr/bin/env python
import socket
import sys
from multiprocessing import Process

def echo_server():
    try :
        my_socket = socket.socket(
            socket.AF_INET,socket.
            SOCK_STREAM,socket.IPPROTO_IP)
    except socket.error:
        print u"Failed to create socket"
        sys.exit()

    address = ('127.0.0.1', 50000)
    buffsize = 4096
    my_msg = ''

    my_socket.bind(address)
    my_socket.listen(1)
    while True :
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





