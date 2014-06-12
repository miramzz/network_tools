#!/usr/bin/env python
import socket
import sys


def echo_client(message) :
    try :
        my_socket = socket.socket(
            socket.AF_INET,socket.
            SOCK_STREAM,socket.IPPROTO_IP)
    except socket.error:
        print u"Failed to create socket"
        sys.exit()
    try :
        my_socket.connect(('127.0.0.1', 50000))
    except :
        print u"Failed to create a connection"
        sys.exit()

    my_socket.sendall(message)
    buffsize = 32
    tmp_msg = ''
    while True :
        recv_msg = my_socket.recv(buffsize)
        tmp_msg += recv_msg
        if (len(recv_msg) < buffsize):
            break
    try :
        my_socket.close()
    except :
        print u"Connection still alive"
    return unicode(tmp_msg, "UTF-8")


if __name__ == "__main__":
    try :
        data = sys.argv[1].encode('UTF-8')
    except IndexError :
        print u"Enter a message to be sent"
    print echo_client(data)


