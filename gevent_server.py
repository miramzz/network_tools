#!/usr/bin/env python
import socket
import http_header as hh

buffsize = 4096


def server(conn, addr):
    my_msg = ''
    while True:
        chunk = conn.recv(buffsize)
        if (len(chunk) < buffsize):
            my_msg += chunk
            break
    conn.shutdown(socket.SHUT_RD)
    conn.sendall(hh.create_response(my_msg))
    conn.shutdown(socket.SHUT_WR)
    conn.close()


def client():
    my_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP
        )
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.bind(('127.0.0.1', 50000))
    my_socket.listen(1)
    my_response = server(my_socket.accept())
    my_response.close()
    return my_response


if __name__ == "__main__":
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server_ = StreamServer(('127.0.0.1', 50000), server)
    server_.serve_forever()
