from http_header import create_response
import gevent_server

date_time = "2014-06-12 16:39:06.162234"

content = b"""----.DS_Store\r
----a_web_page.html\r
----make_time.py\r
----sample.txt\r
----images\r
--------JPEG_example.jpg\r
--------sample_1.png\r
--------Sample_Scene_Balls.jpg\r
----JPEG_example.jpg\r
----sample_1.png\r
----Sample_Scene_Balls.jpg
"""


def http_msg(msg_type, cont_len, cont_type):
    byte_string = b"""HTTP/1.1 {}\r
Date: {}\r
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r
Etag: "3f80f-1b6-3e1cb03b"\r
Accept-Ranges:  none\r
Content-Length: {}\r
Connection: close\r
Content-Type: {}; charset=UTF-8\r\n\r\n\r
{}""".format(msg_type, date_time, cont_len, cont_type, content)
    return byte_string


def err_msg(msg_type):
    byte_string = b"""\
HTTP/1.1 {}\r\n\
Date: {}\r\n\
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n\
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n\
""".format(msg_type, date_time)
    return byte_string


def test_200_OK():
    msg = b"""\
GET / HTTP/1.1\r\n
Host: www.example.com\r\n\r\n
"""
    assert create_response(msg) == http_msg('200 OK', 230, 'None')


def test_get():
    msg = b"""\
PUT / HTTP/1.1\r\n
Host: www.example.com\r\n\r\n
<CRLF>"
"""
    assert create_response(msg) == err_msg('405 Method Not Allowed')


def test_uri():
    msg = b"""\
GET /index.html HTTP/1.1\r\n
Host: www.example.com\r\n\r\n
<CRLF>"
"""
    assert create_response(msg) == err_msg('404 Page Not Found')


def test_protocol():
    msg = b"""\
GET / HTTP/1.0\r\n
Host: www.example.com\r\n\r\n
<CRLF>"
"""
    assert create_response(msg) == err_msg('400 Bad Request')


def test_protocol2():
    msg = b"""\
GET / HTP\r\n
Host: www.example.com\r\n\r\n
<CRLF>"
"""
    assert create_response(msg) == err_msg('400 Bad Request')
