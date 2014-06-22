from http_header import create_response


def http_msg(msg_type, cont_len, cont_type, content):
    date_time = "2014-06-12 16:39:06.162234"
    byte_string = b"""\
HTTP/1.1 {}\r\n\
Date: {}\r\n\
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n\
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n\
Etag: "3f80f-1b6-3e1cb03b"\r\n\
Accept-Ranges:  none\r\n\
Content-Length: {}\r\n\
Connection: close\r\n\
Content-Type: {}; charset=UTF-8\r\n\r\n\
{}
""".format(msg_type, date_time, cont_len, cont_type, content)
    return byte_string


def test_200_OK():
    # test if it is working
    msg = b"""\
GET / HTTP/1.1\r\n\
Host: www.example.com\r\n\r\n\
"""
    assert create_response(msg) == http_msg('200 OK', 0, 'None', '')


def test_get():
    # method test if we send PUT instead of GET
    msg = b"""\
PUT / HTTP/1.1\r\n\
Host: www.example.com\r\n\
"""
    assert create_response(msg) == http_msg(
        '405 Method Not Allowed', 0, 'None', '')


def test_uri():
    # uri test if we send not root
    msg = b"""\
GET /index.html HTTP/1.1\r\n\
Host: www.example.com\r\n\
"""
    assert create_response(msg) == http_msg(
        "405 Method Not Allowed", 0, 'None', '')


def test_protocol():
    # protocol test if we send 1.0
    msg = b"""\
GET / HTTP/1.0\r\n\
Host: www.example.com\r\n\
"""
    assert create_response(msg) == http_msg(
        "400 Bad Request", 0, 'None', '')


def test_protocol2():
    # protocol test if we don't send http/1.1
    msg = b"""\
GET / HTP\r\n\
Host: www.example.com\r\n\
"""
    assert create_response(msg) == http_msg(
        "400 Bad Request", 0, 'None', '')
