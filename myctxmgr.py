#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ContextManager(object):
    """コンテキストマネージャとして動作するクラス"""

    def __enter__(self):
        # with文のブロックの前に実行される処理
        print('Before processing')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with文のブロックの後に実行される処理
        print('After processing')


def main():
    with ContextManager():
        # この処理の前後に処理が挿入される
        print('Hello, World!')


if __name__  == '__main__':
    main()

