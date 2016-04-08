#!/usr/bin/env python
# -*- coding: utf-8 -*-


from contextlib import contextmanager

@contextmanager
def context_manager():
    """コンテキストマネージャとして動作するジェネレータ"""

    # with文のブロック前に実行される処理
    print('Before processing')
    try:
        # with文のブロックの中身に相当する処理
        yield
    finally:
        # with文のブロックの後で実行される処理
        print('After processing')


def main():
    with context_manager():
        print('Hello, World!')


if __name__ == '__main__':
    main()

