#!/usr/bin/env python
import os
import sys
import socket
import http_header as hh
from multiprocessing import Process



def echo_server():
    my_socket = socket.socket(
    socket.AF_INET,socket.
    SOCK_STREAM,socket.IPPROTO_IP)

    address = ('127.0.0.1', 5000)
    buffsize = 32

    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.bind(address)
    my_socket.listen(1)
    while True :
        my_msg = ''
        conn, client_add = my_socket.accept()
        while  True:
            recv_msg = conn.recv(buffsize)
            my_msg += recv_msg
            if (len(recv_msg) < buffsize):
                break
        conn.sendall(hh.create_uri_request(my_msg))
        conn.shutdown(socket.SHUT_WR)
        conn.close()

    my_socket.close()

if __name__=="__main__":
    # p = Process(target=echo_server)
    # p.start()
    # p.join()
    print hh.create_uri_request(b"GET /Users/muazzezmira/Desktop/webroot/sample.txt HTTP/1.1\r\nHost: www.mysite1.com:80")
    #print hh.create_uri_request(b"GET /Users/muazzezmira/Desktop/webroot HTTP/1.1\r\nHost: www.mysite1.com:80")


