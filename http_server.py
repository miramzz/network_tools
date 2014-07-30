#!/usr/bin/env python
import socket
import http_header as hh


def echo_server():
    try:
        my_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_IP
        )
    except socket.error:
        print 'Unable to create socket'

    address = ('127.0.0.1', 5000)
    buffsize = 4096

    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.bind(address)
    my_socket.listen(1)
    while True:
        my_msg = ''
        try:
            conn, client_add = my_socket.accept()
        except socket.error:
            print 'Unable to make a connection'
        while True:
            recv_msg = conn.recv(buffsize)
            my_msg += recv_msg
            if "\r\n\r\n" in recv_msg:
                break

        # conn.shutdown(socket.SHUT_RD)
        conn.sendall(hh.create_response(my_msg))
        # conn.shutdown(socket.SHUT_WR)
        conn.close()

    my_socket.close()

if __name__ == "__main__":
    echo_server()
# print hh.create_uri_request(b"GET / HTTP/1.1\r\nHost: www.mysite1.com:80")
# print hh.create_uri_request(b"GET /Users/muazzezmira/Desktop/
# webroot HTTP/1.1\r\nHost: www.mysite1.com:80")
