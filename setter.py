#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyClass(object):

    def __init__(self):
        self._n = 0

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = value * 2


def main():
    obj = MyClass()
    obj.n = 100
    print(obj.n)

if __name__ == '__main__':
    main()

