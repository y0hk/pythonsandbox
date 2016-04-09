#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SuperClass(object):
    """スーパークラスに見立てたクラス"""

    def greet(self):
        """サブクラスでオーバーライドするインターフェース"""
        print('Super')


class DuckSubClass(object):
    """ダックタイピングでSuperClassとして振る舞う"""

    def greet(self):
        print('Sub')


def main():
    # DuckSubClassはSuperClassのように振る舞う
    # しかし、継承関係ではないのでisinstance()はFalse
    obj = DuckSubClass()
    obj.greet()
    print(isinstance(obj, SuperClass))


if __name__ == '__main__':
    main()

