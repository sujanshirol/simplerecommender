# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:45:08 2021

@author: sshir
"""

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '0.0.1'
DESCRIPTION = 'Items recommendation for a specific user'


setup(
    name="simplerecommender",
    version=VERSION,
    author="Sujan Shirol",
    author_email="<sshirol73@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/sujanshirol/simplerecommender',
    keywords=['python', 'recommendation algorithm', 'recommender', 'recommendation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={'': 'src'},
    py_modules = ['simplerecommender']
)
