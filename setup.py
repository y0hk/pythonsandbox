#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from setuptools import find_packages


def main():
    setup(
        name='package101',
        version='0.0.1',
        description='My first package',
        author='your name',
        author_email='email@example.jp',
        packages=find_packages()
        )



if __name__ == '__main__':
    main()

