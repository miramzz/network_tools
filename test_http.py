from http_server import create_response
import os
import sys




def test_no_GET_tag():
    try:
        create_response(u"GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80")
    except :
        err = sys.exc_info()[0]









