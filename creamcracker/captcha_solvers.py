from deathbycaptcha import SocketClient


class CaptchaSolver(object):

    def __init__(self):
        self._client = None


class DBCSolver(CaptchaSolver):
    """
    DeathByCaptcha API interfacer.

    param: file_path (str)
    param: credentials (tuple (username, password))
    param: timeout (int)
    """

    @property
    def client(self):
        if self._client is None:
            self._client = SocketClient(*self.credentials)
        return self._client

    def __call__(self, file_path, credentials=(), timeout=20):
        self.credentials = credentials
        response = self.client.decode(file_path, timeout)
        return response['text']


class IcebreakerSolver(CaptchaSolver):

    @property
    def client(self):
        pass

    def __call__(self):
        raise NotImplementedError(
            'Icebreaker captcha solver must be implemented.')


death_by_captcha = DBCSolver()
icebreaker = IcebreakerSolver()
