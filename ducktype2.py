#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

# 仮想的サブクラスを登録したいクラスにはABCMetaを指定
class SuperClass(metaclass=abc.ABCMeta):
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
    # 継承関係がなくても仮想的サブクラスに登録しているので
    # isinstance()はTrue
    obj = DuckSubClass()
    obj.greet()
    print(isinstance(obj, SuperClass))


if __name__ == '__main__':
    main()

