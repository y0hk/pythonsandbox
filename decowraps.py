#!/usr/bin/env python
# -*- coding: utf-8 -*-


def swap(func):
    """中身をすり替えるだけで何もしないデコレータ"""
    def _swap(*args, **kwargs):
        """さようなら！"""
        return func(*args, **kwargs)
    return _swap


def greet1():
    """こんにちは！"""
    print('Hello, World!')


@swap
def greet2():
    """こんにちは"""
    print('Hello, World!')


def main():
    print(greet1.__doc__)
    print(greet2.__doc__)


if __name__ == '__main__':
    main()

