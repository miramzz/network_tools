import os
import datetime
import mimetypes

# sudo lsof -n | grep LISTEN

_err_tags = {400:'Bad Request',
            403:'Forbidden',
            404:'Page Not Found',
            405:'Method Not Allowed',
            408:'Request Timeout',
            429:'Too Many Requests',
            444:'No Response',
            500:'Internal Server Error',
            200:'OK'}

_http_tags = {}

def create_http_request():
    _http_tags['date_time'] = '2014-06-12 16:39:06.162234'
    #_http_tags['date_time'] = datetime.datetime.now()
    byte_string = b"""\
HTTP/1.1 {msg_code}\r\n\
Date: {date_time}\r\n\
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n\
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n\
Etag: "3f80f-1b6-3e1cb03b"\r\n\
Accept-Ranges:  none\r\n\
Content-Length: 438\r\n\
Connection: close\r\n\
Content-Type: {cont_type}; charset=UTF-8\r\n\r\n\
{content}
""".format(**_http_tags)
    return byte_string

def list_dirs():
    uri = _http_tags['uri']
    _l = []
    for dirpath, _dirs, files in os.walk(uri):
        for _file in files:
            _tmp = os.path.join(dirpath, _file)
        _l.append(_tmp)
    _http_tags['content'] = '<html><h1>{}</h1></html>'.format(_l)
    print _l

def check_uri_resource():
    uri = _http_tags['uri']
    file_name = os.path.split(uri)[1]

    if os.path.isdir(_http_tags['uri']):
        list_dirs()
    elif not os.path.exists(uri) :
        return 404
    else  :
        msg_cont = open(uri,'rb').read()
        _http_tags['content'] = '<html><h1>{}</h1></html>'.format(msg_cont)

    _http_tags['cont_type'] = mimetypes.guess_type(file_name)[0]


def check_request_method():
    if _http_tags['method'] != 'GET':
        return 405

def check_request_uri():
    if _http_tags['uri'][0] != '/':
        return  404
    _http_tags['uri'] = "webroot"+uri

def check_request_protocol():
    if _http_tags['protocol'] != 'HTTP/1.1':
        return  400

def check_err_response():
    _error_code = 0
    check_list = 0
    try :
        check_list = [check_request_method(), check_request_protocol(),
                      check_request_uri(), check_uri_resource()]
    except :
        pass

    if max(check_list) :
        _error_code = filter(lambda x : x is not None, check_list).pop(0)

    if _error_code :
        err_msg = '{} {}'.format(_error_code, _err_tags.get(_error_code))
        _http_tags['msg_code'] = err_msg
    else :
        _http_tags['msg_code'] = '200 OK'


def create_uri_request(recv_msg):
    #import pdb; pdb.set_trace()
    recv_msg = recv_msg.split('\r\n')
    _http_tags['method'], _http_tags['uri'], _http_tags['protocol'] = recv_msg[0].split()[:3]

    for item in recv_msg[1:]:
        if 'host:' == item.lower().split()[0]:
            _http_tags['Host'] = item.split()[1]
            break
    check_err_response()
    return create_http_request()



