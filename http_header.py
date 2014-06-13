import os
import sys
import datetime

# sudo lsof -n | grep LISTEN

err_tags = {400:'Bad Request',
            403:'Forbidden',
            404:'Page Not Found',
            405:'Method Not Allowed',
            408:'Request Timeout',
            429:'Too Many Requests',
            444:'No Response',
            500:'Internal Server Error',
            200:'OK'}

file_extensions = ('txt', 'jpeg', 'jpg', 'py', 'png', 'html')


def list_dirs(uri):
    _l = []
    for dirpath, _dirs, files in os.walk(uri):
        for _file in files:
            _tmp = os.path.join(dirpath, _file)
        _l.append(_tmp)
    return _l

def msg_content(uri):
    f = open(uri,'rb').read()
    return f

def create_body(ind_type, dirs_list = None, msg_content = None):
    if dirs_list:
        return dirs_list, ind_type
    return msg_content, ind_type


def check_uri_resource(uri):
    #file_name = os.path.abspath(uri).split('\\')[-1]
    file_name = os.path.split(uri)[1]
    ind_type = file_name.split('.')[-1]

    #return msg_content("/Users/muazzezmira/Desktop/webroot 2/sample.txt", ind_type)

    if os.path.isdir(uri):
        l = list_dirs(uri)
    elif not os.path.exist(uri) :
        #return 404
        pass
    else :
        # return content of the file
        msg_cont = msg_content(uri)
    return (ind_type, l, msg_cont)



def create_http_request(msg_type):
    #date_time = '2014-06-12 16:39:06.162234'
    date_time = datetime.datetime.now()
    byte_string = """\
HTTP/1.1 {}\r\n\
Date: {}\r\n\
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n\
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n\
Etag: "3f80f-1b6-3e1cb03b"\r\n\
Accept-Ranges:  none\r\n\
Content-Length: 438\r\n\
Connection: close\r\n\
Content-Type: text/html; charset=UTF-8\r\n\r\n\
<CRLF>\
""".format(msg_type, date_time)
    print byte_string
    return bytearray(byte_string)

def check_request_method(method):
    if method.upper() != 'GET':
        return 405

def check_request_uri(uri):
    if uri != "/":
        return 405

def check_request_protocol(protocol):
    if protocol.upper() != 'HTTP/1.1':
        return 400

def check_request_host(host):
    if host :
        return 0

def check_err_response(method,uri,protocol,host):
    if check_request_method(method):
        err_code = check_request_method(method)
    elif check_request_uri(uri):
        err_code = check_request_uri(uri)
    elif check_request_protocol(protocol):
        err_code = check_request_protocol(protocol)
    else:
        err_code = check_request_host(host)

    if err_tags.has_key(err_code) :
        err_message = "{} {}".format(err_code, err_tags.get(err_code))
        raise NameError(err_message)

def create_err_respond(err_code):
    return create_http_request(err_code)

def create_ok_respond():
    return create_http_request('200 OK')

def create_uri_request(recv_msg):
    recv_msg = recv_msg.split('\r\n')
    method, uri, protocol = recv_msg[0].split()[:3]

    return check_uri_resource(uri)

    for item in recv_msg[1:]:
        if 'host:' == item.lower().split()[0]:
            host = item.split()[1]
            break

    try:
        check_err_response(method, uri, protocol, host)
    except:
        err_code = sys.exc_info()[1]
        return create_err_respond(err_code)
    else:
        return create_ok_respond()