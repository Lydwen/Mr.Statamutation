#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import statapython

setup(
    name='statapython',
    version=statapython.__version__,

    description="Mr.Statamutation build chain system (mutate, test, report).",
    long_description=open('../README.md').read(),

    author="Mr.Statamutation Team",
    url="https://github.com/Lydwen/Mr.Statamutation/tree/master/Mr.Statapython",

    packages=find_packages(),
    package_data={
        'statapython.templates': ['*.html', '*.css']
    }
)
