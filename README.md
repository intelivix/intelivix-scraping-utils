# intelivix-scraping-utils

### CreamCracker
Set of captcha solvers that wrap different APIs.
Covered APIs:
* DeathByCaptcha  - http://deathbycaptcha.com

#### Usage
#
```python
from creamcracker import death_by_captcha

credentials = (username, password)
timeout = 20
death_by_captcha('file_path/captcha.png', credentials, timeout)
> u'ef8brn'
```
