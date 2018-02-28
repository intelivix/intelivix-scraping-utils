from enums import SpiderStatus
from enums import InstanciaStatus

KEY_FILE_DICT = {
    "type": "service_account",
    "project_id": "tribunais-coverage",
    "private_key_id": "63af524a6aec32b4682b8c3a55050df55c3faa4e",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCX4q0FaQxQU3C/\nwn2gRF9cTDfj/VG+DO0sRrORk1G4LoYrMqMZ9q0EHz7zsbsSfysxb6Tr7IbgeH7q\n3AtuLhT9F/JFumu52hL3r2WdyuDDc+J68y7PpjpoKl6tszVf9+g7HKekHwkAa6uR\nkF2glnmmjeH3I44rWmGC97V5I+qOrXCa1Xr4evvjUJnc5Kda0/VvV+it0UuSvyph\ncb8rqjjuQQNpSLSbpif6rCCROVzR7zOIpZUxaSpk9j4xmJrNLyliKCwkdL6QiEz9\noF3y9+7PZoB+/ZCZrSTaLta92jK8+gzncH46HOoB5wpwkrR5JQfh+GM3dsLWt79Q\nOO3cnozvAgMBAAECggEAQEFb3E2YMYVTTjTMK9ixFR2DiZbaFZJnZhNVFXGjIU3B\nYhYOjUXf5T4IxlT65PTaw5PNTCfo2Z7wZpCH32lsZLRUQO6Ac4RQAOv5i9tP4jAs\n8MHfnGZhED9YhZiqrHp3C0bwnwyoJL7oOvE9wtnWBkHBBmpK04ltdlgwNFse+JO9\nly8WvmXhZwvfzF/hMQXicgiLZgYzVrYKY/P7E+BTAipo5Aw/XYfDR1l5Kbpimctu\nYzhd7XUD6mxi+DcGG7qfwJAq4a2H5WbSEfwYzfcXX7F+3pJVo5rW9Md2TCYkvigX\n7RJYbq4acuqJi0beDHBuvY4XNsL+xcrnMEwnYpqISQKBgQDF0017FtoJ73cMXMGL\ne/GFHHeAJkwumLfACBhdtwU1oksbpl0NKu2ldbBD4gXrtPY26ZVzTS4DFylzN0TE\nKqXPzJZUkLIVTCh3+9WJHCKEaVEOg+89PBL/n+NJMaaSW6jaWm4/2wWspclqP15G\nrZ46DAuisiFOkk0ysZPzfDIziQKBgQDEjOu08rDZ+WDIFrC5pZmWdCdeETwhFOwb\nVZ67d/JIkMvQf5D+CZ/RItJMQjbed45tZXs4QHRejDqJhFIENpBah2k6xwQDrSOM\nL2YnEQOdxneznsHaVcgan0Dt4OLZaqPI3mFIYoLsOdie11sKNKKI6vbxdYdpOeEZ\n9l9JlTKGtwKBgFgFNKxX9pwFGIs/mj5d35DCock7QRpaiSfAclcAYCkFFTYwR6bc\nOvEr9Em//7JoykSUmhK7fIWTgLXrGYXPFAfpl9n4p8QiJr98Jf7jrdgMpCw5N/Gf\nETT8Bz1CAkOM1QySwAtZgKTY/01u9JuuFIDvax3w9DDpl7++k336/LtBAoGBAIp0\nkp3W0Anch/arNTaxlu3LSOgUz/yl1mSy/awlpIDFry1ij2rEsNYL54RcqHYyVhxt\n/kzz6oWn1pyEn5nkLe/3r4L+Kq/ESWQ5B4bBj4CXDD91uCzrfJh0UrK/Vk29tz6K\nmJD7BCsP3K6YGcOorE4y5l3VYtwXL6CwUxNsjDklAoGAIsSIwiAVC0Jaoi91r/38\n6szCV4B2fji5RQJ+MAC0anQ5UfDH14vVI5zFmchJIBFx2G3IpR9jbz/wS0/pVo8+\nAeRVrLqhTs9V7CzMLJxONkFy1FDfKh14LY1Gp9zFCHbXRXX7PdLJZr2k0YOgUFgQ\nC2gDysZ/w5dR7yxoXnHyGlU=\n-----END PRIVATE KEY-----\n",
    "client_email": "robo-intelivix@tribunais-coverage.iam.gserviceaccount.com",
    "client_id": "104307854629982139866",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/robo-intelivix%40tribunais-coverage.iam.gserviceaccount.com"
}

ESTADOS_BRASIL = [
    'GO', 'MT', 'MS', 'DF', 'AM', 'AC', 'RO', 'RR',
    'AP', 'TO', 'PA', 'MA', 'PI', 'CE', 'RN', 'PB',
    'PE', 'SE', 'AL', 'BA', 'SP', 'MG', 'RJ', 'ES',
    'PR', 'SC', 'RS']

DEFAULT_COVERAGE = {
    'status': SpiderStatus.NAO_IMPLEMENTADO,
    'captcha': False,
    'arquivos': False,
    '1-grau-fisico': InstanciaStatus.NAO_IMPLEMENTADO,
    '2-grau-fisico': InstanciaStatus.NAO_IMPLEMENTADO,
    '1-grau-eletronico': InstanciaStatus.NAO_IMPLEMENTADO,
    '2-grau-eletronico': InstanciaStatus.NAO_IMPLEMENTADO,
    'jec-1-grau-fisico': InstanciaStatus.NAO_IMPLEMENTADO,
    'jec-2-grau-fisico': InstanciaStatus.NAO_IMPLEMENTADO,
    'jec-1-grau-eletronico': InstanciaStatus.NAO_IMPLEMENTADO,
    'jec-2-grau-eletronico': InstanciaStatus.NAO_IMPLEMENTADO,
}
