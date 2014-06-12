#!/usr/bin/env python
import os
import sys
import time
import datetime
import socket
from multiprocessing import Process


err_tags = {400:'Bad Request',
            403:'Forbidden',
            404:'Page Not Found',
            408:'Request Timeout',
            429:'Too Many Requests',
            444:'No Response',
            500:'Internal Server Error',
            200:'OK'}

def create_http_request(msg_type):
    date_time = datetime.datetime.now()
    byte_string = b"""\
HTTP/1.1 {}\r\n\
Date: {}\r\n\
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n\
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n\
Etag: "3f80f-1b6-3e1cb03b"\r\n\
Accept-Ranges:  none\r\n\
Content-Length: 438\r\n\
Connection: close\r\n\
Content-Type: text/html; charset=UTF-8\r\n\r\n""".format(msg_type, date_time)
    return byte_string

def check_request_method(method):
    if method.upper() != 'GET':
        return 500

def check_request_uri(uri):
    if uri.upper() != 'something':
        return 400

def check_request_protocol(protocol):
    if protocol.upper() != 'HTTP/1.1':
        return 400

def check_request_host(host):
    if host :
        return 0

def check_err_response(method,uri,protocol,host):
    if check_request_method(method):
        err_code = check_request_method(method)
    elif check_request_uri(uri):
        err_code = check_request_uri(uri)
    elif check_request_protocol(protocol):
        err_code = check_request_protocol(protocol)
    else:
        err_code = check_request_host(host)

    if err_tags.has_key(err_code) :
        err_message = "{} {}".format(err_code, err_tags.get(err_code))
        raise NameError(err_message)

def create_err_respond(err_code):
    return create_http_request(err_code)

def create_ok_respond():
    return create_http_request('200 OK')

def create_uri_request(recv_msg):
    recv_msg = recv_msg.split('\r\n')
    method, uri, protocol = recv_msg[0].split()[:3]

    for item in recv_msg[1:]:
        if 'host:' == item.lower().split()[0]:
            host = item.split()[1]
    try:
        check_err_response(method, uri, protocol, host)
    except:
        err_code = sys.exc_info()[1]
        return create_err_respond(err_code)
    else:
        return create_ok_respond()


def echo_server():
    my_socket = socket.socket(
    socket.AF_INET,socket.
    SOCK_STREAM,socket.IPPROTO_IP)

    address = ('127.0.0.1', 50000)
    buffsize = 32

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

        conn.sendall(my_msg)
        conn.shutdown(socket.SHUT_WR)
        conn.close()

    my_socket.close()

if __name__=="__main__":
    # p = Process(target=echo_server)
    # p.start()
    # p.join()
    print create_uri_request(b"GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80")



