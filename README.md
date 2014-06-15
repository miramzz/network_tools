<h4>Branch : http1<h4>
<h5>echo_client.py :<br\></h5>
    This is the client side. It creates a socket and make a connection to server side.<br\>
    Limitations :
        Buffersize = 4096.
    Input    : Message
    Output : No Output
    Return value : Sends a http request message to server side<br\>
<h5>http_server.py :<br\></h5>
    This is server side. It creates a socket and process requests.
    Limitetions :
        Buffersize = 4096
    Input    : No input
    Output : No output
    Return value : Creates a Http response message and sends it.
<h5>test_http.py :<br\></h5>
    This is for py.test. There are 5 tests to check the output of the http_server if  :
        - valid scenario is working
        - Http method is wrong
        - Http uri is wrong
        - Http protocol is old version
        - Http protocol is wrong




