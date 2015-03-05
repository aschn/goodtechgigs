#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import goodtechgigs
version = goodtechgigs.__version__

setup(
    name='goodtechgigs',
    version=version,
    author="Anna Schneider",
    author_email='annarschneider@gmail.com',
    packages=[
        'goodtechgigs',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['goodtechgigs/manage.py'],
)
