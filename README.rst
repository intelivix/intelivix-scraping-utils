intelivix-scraping-utils
========================

.. _badges_start:

|Build Status|


CreamCracker
------------
Set of captcha solvers that wrap different APIs. Covered APIs:

    - DeathByCaptcha (http://deathbycaptcha.com)

Usage
'''''

.. code:: python

    from creamcracker import death_by_captcha

    credentials = (username, password)
    timeout = 20
    death_by_captcha('file_path/captcha.png', credentials, timeout)
    > u'ef8brn'


.. _available_badges_start:

.. |Build Status| image:: https://img.shields.io/travis/intelivix/intelivix-scraping-utils.svg?style=flat
   :target: https://travis-ci.org/intelivix/intelivix-scraping-utils
.. |Coverage Status| image:: https://coveralls.io/repos/intelivix/intelivix-scraping-utils/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/intelivix/intelivix-scraping-utils?branch=master

.. _available_badges_end:
