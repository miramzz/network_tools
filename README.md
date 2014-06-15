<h4>Branch : http2<h4>
<h5>http_server.py :<br\></h5>
    This is server side. It creates a socket and process requests.
    Limitations :
        Buffersize = 4096
    Input    : No input
    Output : No output
    Return value : Calls http_header.py to create http response and sends it.
<h5>http_header.py :<br\></h5>
    This header file is to help http_server.py to create the http response. All http related code is in this file
    Limitations : Bytearray checks
    Input : Message
    Output : Parses received message and creates proper http response. 
             In failed cases returns proper Http Error message.
             Depending on uri information in received message :
                Shows all directories recursively
                Shows file content depending on file type
<h5>test_http.py :<br\></h5>
    This is for py.test. There are 5 tests to check the output of the http_server if  :
        - valid scenario is working
        - Http method is wrong
        - Http uri is wrong
        - Http protocol is old version
        - Http protocol is wrong
