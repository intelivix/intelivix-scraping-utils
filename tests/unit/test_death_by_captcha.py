from mock import Mock
from creamcracker import death_by_captcha
from creamcracker.deathbycaptcha import SocketClient


def test_solve_captcha():
    SocketClient.decode = Mock()
    SocketClient.decode.return_value = {'text': 'abc123'}
    credentials = ('username', 'password')

    response = death_by_captcha(
        '../captcha.png', credentials, timeout=20)

    assert death_by_captcha.client.__class__ is SocketClient
    assert death_by_captcha.credentials == credentials
    assert response['text']  == 'abc123'
