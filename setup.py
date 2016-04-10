#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from setuptools import find_packages


def main():
    setup(
        name='package101',
        version='0.0.3',
        description='My first package',
        author='your name',
        author_email='email@example.jp',
        packages=find_packages(),
        install_requires=[
            'requests'
            ],
        entry_point={
            'console_scripts': [
                'greet = package101:greet'
                ]
            }
        )


if __name__ == '__main__':
    main()

