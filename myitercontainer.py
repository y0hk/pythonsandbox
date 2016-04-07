#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class MyContainer(object):
    """ 連続した整数を返すイテレータのコンテナクラス"""
    def __init__(self, stop=-1, start=0):
        self.stop = stop
        self.start = start

    def __iter__(self):
        """イテレータオブジェクトを作って返す"""
        return MyIterator(self.stop, self.start)

class MyIterator(object):
    """連続した整数を返すイテレータクラス"""
    def __init__(self, stop=-1, start=0):
        self.stop = stop
        self._current = start

    def __iter__(self):
        """イテレータオブジェクトを返す
        ここではselfを返答
        """
        return self

    def __next__(self):
        """次に取り出す要素を返す
        次の要素がなければStopIteration例外
        """
        if self._current >= self.stop:
            raise StopIteration()
        result = self._current
        self._current += 1
        return result

    def next(self):
        # Python 2.xでは__next__()→next()が必要になる
        return self.__next__()

def main():
    it = MyContainer(10)
    for _ in range(2):
        #　コンテナオブジェクトが複数回forで回される
        for i in it:
            print(i, end=' ')
        print()

if __name__ == '__main__':
    main()

