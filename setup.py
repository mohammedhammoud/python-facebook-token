# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='facebooktoken',
    version='0.0.1',
    author=u'Mohammed Hammoud',
    author_email='mohammed@iktw.se',
    packages=find_packages(),
    url='https://github.com/iktw/python-facebook-token',
    license='MIT licence, see LICENCE.txt',
    description='Lightweight library for refreshing your facebook access token.',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'requests',
    ],
)