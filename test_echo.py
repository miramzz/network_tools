import pytest
import socket
from os import urandom
from echo_client import echo_client


def test_echo():
    assert echo_client('Test message') == 'Test message'


def test_random():
    test1 = urandom(100)
    assert echo_client(test1) == test1


def test_string():
    assert echo_client(u"Enter a message to be sent") == \
        'Enter a message to be sent'


def test_long():
    long_msg = b'\x00'*31
    assert echo_client(long_msg) == long_msg


def test_error():
    with pytest.raises(socket.error):
        echo_client(u"Eot test is done")
