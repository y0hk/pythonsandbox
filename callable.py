#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CallableClass(object):

    def __call__(self, msg):
        """このメソッドを実装することでオブジェクトが呼び出し可能となる"""
        print(msg)


def main():
    # objはCallableClassのインスタンス
    obj = CallableClass()
    # しかし、関数のように実行できる
    obj('Hello, World!')


if __name__ == '__main__':
    main()


