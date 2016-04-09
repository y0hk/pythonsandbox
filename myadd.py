#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """self + otherするときに呼ばれる"""
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        """str(self)するときに呼ばれる"""
        return '<Point x:{x} y:{y}>'.format(
                x = self.x,
                y = self.y
                )


def main():
    p1 = Point(100, 100)
    p2 = Point(50, 50)
    p3 = p1 + p2
    print(p3)

if __name__ == '__main__':
    main()


