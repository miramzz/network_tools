#!/usr/bin/env python
import socket
import sys


def echo_client(message):
    try:
        my_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP
            )
    except socket.error:
        sys.exit()
    try:
        my_socket.connect(('127.0.0.1', 5000))
    except:
        sys.exit()

    my_socket.sendall(message)
    buffsize = 32
    tmp_msg = ''
    while True:
        recv_msg = my_socket.recv(buffsize)
        tmp_msg += recv_msg
        if (len(recv_msg) < buffsize):
            print recv_msg
            break
    try:
        my_socket.close()
    except:
        print u"Connection still alive"
    return bytearray(tmp_msg)


def create_conn():
    try:
        my_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP
            )
    except socket.error:
        sys.exit()

    try:
        my_socket.connect(('127.0.0.1', 5000))
    except:
        sys.exit()


def send_msg(message):
    print "zz"
    my_socket.sendall(message)
    buffsize = 32
    tmp_msg = ''
    while True:
        recv_msg = my_socket.recv(buffsize)
        tmp_msg += recv_msg
        if (len(recv_msg) < buffsize):
            print recv_msg
            break
    try:
        my_socket.close()
    except:
        print u"Connection still alive"
    print tmp_msg
    return bytearray(tmp_msg)


if __name__ == "__main__":
    try:
        data = sys.argv[1]
    except IndexError:
        print u"Enter a message to be sent"
    echo_client(bytearray(data))
