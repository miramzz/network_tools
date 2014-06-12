from http_server import create_uri_request
import os
import sys
import datetime



def http_msg(msg_type):
    date_time = "2014-06-12 16:39:06.162234"
    byte_string = b"""\
HTTP/1.1 {}\r\n\
Date: {}\r\n\
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n\
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n\
Etag: "3f80f-1b6-3e1cb03b"\r\n\
Accept-Ranges:  none\r\n\
Content-Length: 438\r\n\
Connection: close\r\n\
Content-Type: text/html; charset=UTF-8\r\n\r\n\
""".format(msg_type, date_time)
    return byte_string


# test if it is working
def test_200_OK():
    msg = """\
GET / HTTP/1.1\r\n\
Host: www.example.com\r\n\
<CRLF>"
"""
    assert create_uri_request(bytearray(msg)) == http_msg("200 OK")

# method test if we send PUT instead of GET
def test_get():
    msg = """\
PUT / HTTP/1.1\r\n\
Host: www.example.com\r\n\
<CRLF>"
"""
    assert create_uri_request(bytearray(msg)) == http_msg("405 Method Not Allowed")

# uri test if we send not root
def test_uri():
    msg = """\
GET /index.html HTTP/1.1\r\n\
Host: www.example.com\r\n\
<CRLF>"
"""
    assert create_uri_request(bytearray(msg)) == http_msg("405 Method Not Allowed")

# protocol test if we send 1.0
def test_protocol():
    msg = """\
GET / HTTP/1.0\r\n\
Host: www.example.com\r\n\
<CRLF>"
"""
    assert create_uri_request(bytearray(msg)) == http_msg("400 Bad Request")


# protocol test if we don't send http/1.1
def test_protocol2():
    msg = """\
GET / HTP\r\n\
Host: www.example.com\r\n\
<CRLF>"
"""
    assert create_uri_request(bytearray(msg)) == http_msg("400 Bad Request")




