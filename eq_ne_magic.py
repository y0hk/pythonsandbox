#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyClass(object):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        # 自作クラスのインスタンスで==演算を使えるようにするため__eq__()の実装
        if not issubclass(other.__class__, MyClass):
            return False

        return self.name == other.name

    def __ne__(self, other):
        # 自作クラスのインスタンスで!=演算を使えるようにするため__ne__()の実装
        return not self.__eq__(other)


def main():
    o1 = MyClass('Foo')
    o2 = MyClass('Bar')
    o3 = MyClass('Foo')

    result = o1 == o2
    print('o1 == o2: {result}'.format(result=result))
    result = o1 == o3
    print('o1 == o3: {result}'.format(result=result))
    result = o1 != o3
    print('o1 != o3: {result}'.format(result=result))


if __name__ == '__main__':
    main()


