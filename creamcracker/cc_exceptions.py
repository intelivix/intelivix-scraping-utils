
class CaptchaTranslationError(Exception):

    def __init__(self, value=None):
        if value:
            self.value = value
        else:
            self.value = 'Could not break captcha.'
