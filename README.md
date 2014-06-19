network_tools
=============

##Echo Server
  - Input : No Input
  - Output : No Output
  - Limitations : Buffersize is 32-bits
  - Server starts listening the socket and waits for any request
  - Checks the request message and sends the request as response
  - Shuts the connection
  - Waits until Key interruption for any request
  - When Key Interruption occurs, server closes the socket

##Echo Client
  - Input : No Input
  - Output : No Output
  - Limitations : Buffersize is 32-bits
  - Echo server connects to server
  - Sends the input message to the server
  - Listens response from server side and prints out the message
  - Closes the connection


