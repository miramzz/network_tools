Branch : http1

echo_client.py :\r\n
    This is the client side. It creates a socket and make a connectiont o server side.
    Limitations :
        Buffersize = 4096.
    Input    : Message
    Output : No Output
    Return value : Sends a http request message to server side
http_server.py :
    This is server side. It creates a socket and process requests.
    Limitetions :
        Buffersize = 4096
    Input    : No input
    Output : No output
    Return value : Creates a Http response message and sends it.
test_http.py :
    This is for py.test. There are 5 tests to check the output of the http_server when  :
        - valid scenario is workin
        - Http method is wrong
        - Http uri is wrong
        - Http protocol is old version
        - Http protocol is wrong




