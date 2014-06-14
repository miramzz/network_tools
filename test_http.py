from http_server import create_uri_request

def http_msg(msg_type):
    date_time = "2014-06-12 16:39:06.162234"
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


# test if it is working
def test_200_OK():
    msg = bytearray("""\
GET / HTTP/1.1\r\n
Host: www.example.com\r\n\r\n
""")
    assert create_uri_request(msg) == http_msg('200 OK')

# method test if we send PUT instead of GET
def test_get():
    msg = b"""\
PUT / HTTP/1.1\r\n
Host: www.example.com\r\n\r\n
<CRLF>"
"""
    assert create_uri_request(msg) == http_msg('405 Method Not Allowed')

# uri test if we send not root
def test_uri():
    msg = b"""\
GET /index.html HTTP/1.1\r\n
Host: www.example.com\r\n\r\n
<CRLF>"
"""
    assert create_uri_request(msg) == http_msg('405 Method Not Allowed')

# protocol test if we send 1.0
def test_protocol():
    msg = b"""\
GET / HTTP/1.0\r\n
Host: www.example.com\r\n\r\n
<CRLF>"
"""
    assert create_uri_request(msg) == http_msg('400 Bad Request')


# protocol test if we don't send http/1.1
def test_protocol2():
    msg = b"""\
GET / HTP\r\n
Host: www.example.com\r\n\r\n
<CRLF>"
"""
    assert create_uri_request(msg) == http_msg('400 Bad Request')




