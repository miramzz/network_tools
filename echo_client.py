#!/usr/bin/env python
import socket
import sys


def echo_client(message) :
    """Creates a connection on the local host
        and sends back the received message
    """
    try :
        my_socket = socket.socket(
            socket.AF_INET,socket.
            SOCK_STREAM,socket.IPPROTO_IP)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()
    try :
        my_socket.connect(('127.0.0.1', 5000))
    except :
        print 'Failed to make a connection'
        sys.exit()

    my_socket.sendall(message)
    buffsize = 4096
    tmp_msg = ''
    while True :
        recv_msg = my_socket.recv(buffsize)
        tmp_msg += recv_msg
        if (len(recv_msg) < buffsize):
            break
    try :
        my_socket.close()
    except socket.error:
        print 'Connection is still alive'
    return bytearray(tmp_msg)


if __name__ == "__main__":
    try :
        data = sys.argv[1]
    except IndexError :
        print 'Enter a message to send'
    print echo_client(bytearray(data))


