#!/usr/bin/env python
import sys
import datetime
import socket

# sudo lsof -n | grep LISTEN

err_tags = {400:'Bad Request',
            403:'Forbidden',
            404:'Page Not Found',
            405:'Method Not Allowed',
            408:'Request Timeout',
            429:'Too Many Requests',
            444:'No Response',
            500:'Internal Server Error',
            200:'OK'}

def create_http_response(msg_type):
    # this line is for testing
    date_time = '2014-06-12 16:39:06.162234'
    #date_time = datetime.datetime.now()
    byte_string = """\
HTTP/1.1 {}\r\n
Date: {}\r\n
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n
Etag: "3f80f-1b6-3e1cb03b"\r\n
Accept-Ranges:  none\r\n
Content-Length: 438\r\n
Connection: close\r\n
Content-Type: text/html; charset=UTF-8\r\n\r\n
""".format(msg_type, date_time)
    return bytearray(byte_string)

def check_request_method(method):
    if method.upper() != 'GET':
        return 405

def check_request_uri(uri):
    if uri != "/":
        return 405

def check_request_protocol(protocol):
    if protocol.upper() != 'HTTP/1.1':
        return 400

def check_err_response(method,uri,protocol,host):
    err_code = 0
    if check_request_method(method):
        err_code = check_request_method(method)
    elif check_request_uri(uri):
        err_code = check_request_uri(uri)
    elif check_request_protocol(protocol):
        err_code = check_request_protocol(protocol)

    if err_tags.has_key(err_code) :
        err_message = "{} {}".format(err_code, err_tags.get(err_code))
        raise NameError(err_message)

def create_response(recv_msg):
    recv_msg = recv_msg.split('\r\n')
    method, uri, protocol = recv_msg[0].split()[:3]

    for item in recv_msg[1:]:
        if 'host:' == item.lower().split()[0]:
            host = item.split()[1]
            break
    try:
        check_err_response(method, uri, protocol, host)
    except NameError:
        err_code = sys.exc_info()[1]
        return create_http_response(err_code)
    else:
        return create_http_response('200 OK')


def echo_server():
    my_socket = socket.socket(
    socket.AF_INET,socket.
    SOCK_STREAM,socket.IPPROTO_IP)

    address = ('127.0.0.1', 5000)
    buffsize = 4096

    # this line is for macs
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.bind(address)
    my_socket.listen(1)
    while True :
        my_msg = ''
        conn, client_add = my_socket.accept()
        while  True:
            recv_msg = conn.recv(buffsize)
            my_msg += recv_msg
            if "\r\n\r\n" in recv_msg:
                break
        #conn.shutdown(socket.SHUT_RD)
        conn.sendall(create_response(my_msg))
        #conn.shutdown(socket.SHUT_WR)
        conn.close()

    my_socket.close()

if __name__=="__main__":
    echo_server()
    #print create_uri_request(b"GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80")



