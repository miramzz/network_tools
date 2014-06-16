#!/usr/bin/env python

def echo(address, socket):
    buffsize = 4096
    while True:
        data = socket.recv(buffsize)
        if data:
            socket.sendall(data)
        else:
            socket.close()
            break

if __name__=="__main__":
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 5000), echo)
    server.serve_forever()

