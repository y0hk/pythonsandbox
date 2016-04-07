#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyClass(object):
    @classmethod
    def greet(cls):
        # classmethodの場合第一引数はcls
        print('Hello, World!')


def main():
    # クラスメソッドなのでインスタンス化不要
    MyClass.greet()


if __name__ == '__main__':
    main()

