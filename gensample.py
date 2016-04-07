#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.xでprint()使うために必要
from __future__ import print_function

def mygenerator(stop, start=0):
    """連続した整数を返すジェネレータ"""
    current_value = start

    while True:
        # 設定された上限値を超えたらジェネレータを抜ける
        if current_value >= stop:
            break
        # ジェネレータではyieldを使って値を返す
        yield current_value

        current_value += 1
        
def main():
    # ジェネレータオブジェクト取得
    gen = mygenerator(10)
    for i in gen:
        print(i, end=' ')
    print()

if __name__ == '__main__':
    main()
