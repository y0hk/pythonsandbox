#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


# 抽象基底クラスではメタクラスにABCMetaを指定する
# python 3.x ではこのようにメタクラスを指定
class SuperClass(metaclass=abc.ABCMeta):
    """抽象基底クラス"""

    # 抽象メソッドはabstractmethodデコレータで修飾する
    @abc.abstractmethod
    def greet(self):
        """抽象メソッド"""
        pass


# 抽象基底クラスを継承する
class SubClass(SuperClass):
    """具象クラス"""

    # 抽象メソッドを実装する
    def greet(self):
        """具象メソッド"""
        print('Hello, World!')


def main():
    # SubClassで全ての抽象メソッドが実装されているためインスタンス化可能
    obj = SubClass()
    obj.greet()


if __name__ == '__main__':
    main()

