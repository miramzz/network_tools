import pytest
import socket
from os import urandom
from echo_client import echo_client
from echo_server import echo_server



def test_echo():
    #need to awake echo_server here but i couldn't figure out how
    test1 = urandom(100)
    assert echo_client(u"Test message") == u"Test message"
    assert echo_client(test1) == test1
    assert echo_client() == u"Enter a message to be sent"


    with pytest.raises(socket.error):
        echo_client(u"Eot test is done")


