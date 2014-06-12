#!/usr/bin/env python
import os
import datetime

def create_response(err, message):
    msg_list = message.split()
    if msg_list[0] != 'GET' :
        pass
    if msg_list[2] != 'HTTP/1.1':
        pass

   # byte_string = b"""\
#HTTP/1.1 {'msg_type'} \r\nDate: {'date_time'}\r\nServer: {'server_name'}\r\n\
#Last-Modified: {'modify_date'}\r\nEtag:{'etag'}\r\n\r\n"""

    try :
        err
        msg_type = b'200 OK'
    except IndexError :
        msg_type = b'400 Bad Request'
    except AttributeError:
        msg_type = b'500 Internal Server Error'

    date_time = datetime.date.timetuple()
    modify_date = os.path.getmtime()
    print date_time






if __name__=="__main__":

    create_response('IndexError', u"GET /path/to/index.html HTTP/1.1")

    """
    200 OK
    400 Bad Request
    403 Forbidden
    404 Page Not Found
    408 Request Timeout
    429 Too Many Requests
    444 No Response
    500 Internal Server error



    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: "3f80f-1b6-3e1cb03b"
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8
    <CRLF>
    <438 bytes of content>
    """



