import os
import datetime
import mimetypes

# sudo lsof -n | grep LISTEN

_err_tags = {400: 'Bad Request', 403: 'Forbidden', 404: 'Page Not Found',
             405: 'Method Not Allowed', 408: 'Request Timeout',
             429: 'Too Many Requests', 444: 'No Response',
             500: 'Internal Server Error', 200: 'OK'}
_http_tags = {}


def create_http_response():
    if _http_tags['msg_code'] != '200 OK':
        return create_http_err()
    # for tests
    _http_tags['date_time'] = "2014-06-12 16:39:06.162234"
    # _http_tags['date_time'] = datetime.datetime.now()
    _http_tags['cont_len'] = len(_http_tags['content'])
    byte_string = b"""\
HTTP/1.1 {msg_code}\r\n\
Date: {date_time}\r\n\
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n\
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n\
Etag: "3f80f-1b6-3e1cb03b"\r\n\
Accept-Ranges: none\r\n\
Content-Length: {cont_len}\r\n\
Connection: close\r\n\
Content-Type: {cont_type}; charset=UTF-8\r\n\r\n\
{content}
""".format(**_http_tags)
    return byte_string


def create_http_err():
    _http_tags['date_time'] = "2014-06-12 16:39:06.162234"
    byte_string = b"""\
HTTP/1.1 {msg_code}\r\n\
Date: {date_time}\r\n\
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n\
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n\
""".format(**_http_tags)
    return byte_string


indentation = "----"


def list_dirs(uri, l, ind_level):
    for dirpath, _dirs, files in os.walk(uri):
        ind = indentation*ind_level
        for _file in files:
            l.append('{}{}'.format(ind, _file))
        for _dir in _dirs:
            l.append('{}{}'.format(ind, _dir))
            new_dir = dirpath + _dir
            list_dirs(os.path.abspath(new_dir), l, (ind_level+1))


def create_uri_resource():
    uri = str(_http_tags['uri'])
    file_name = os.path.split(uri)[1]

    if os.path.isdir(uri):
        l = []
        list_dirs(uri, l, 1)
        _str = ''
        for item in l:
            _str += '\r\n' + item
        _http_tags['content'] = '{}'.format(_str)
    else:
        msg_cont = open(uri, 'rb').read()
        _http_tags['content'] = msg_cont

    _http_tags['cont_type'] = mimetypes.guess_type(file_name)[0]


def check_uri_resource():
    uri = str(_http_tags['uri'])
    if not os.path.exists(uri):
        return 404


def check_request_method():
    if _http_tags['method'] != 'GET':
        return 405


def check_request_uri():
    if _http_tags['uri'][0] != '/':
        return 404
    _http_tags['uri'] = '/Users/muazzezmira/Desktop/webroot' + \
                        _http_tags['uri']


def check_request_protocol():
    if _http_tags['protocol'] != 'HTTP/1.1':
        return 400


def check_err_response():
    _error_code = 0
    check_list = [check_request_method(), check_request_protocol(),
                        check_request_uri(), check_uri_resource()]

    if max(check_list):
        _error_code = filter(lambda x: x is not None, check_list).pop(0)

    if _error_code:
        err_msg = '{} {}'.format(_error_code, _err_tags.get(_error_code))
        _http_tags['msg_code'] = err_msg
    else:
        create_uri_resource()
        _http_tags['msg_code'] = '200 OK'


def create_response(recv_msg=''):
    recv_msg = recv_msg.split('\r\n')
    _http_tags['method'], _http_tags['uri'], \
        _http_tags['protocol'] = recv_msg[0].split()[:3]

    for item in recv_msg[1:]:
        if 'host:' == item.lower().split()[0]:
            _http_tags['Host'] = item.split()[1]
            break
    check_err_response()
    return create_http_response()
