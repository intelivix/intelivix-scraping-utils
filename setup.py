#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scrapingutils',
    version='0.1',
    description='Set of utils for scraping tasks with python.',
    author='Walter Sobral',
    author_email='wsacin@gmail.com',
    keywords=['captcha', 'deathbycaptcha', 'coverage'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'coveragecsv = scrapingutils.spidercoverage.manager:main',
        ],
    }
    )
