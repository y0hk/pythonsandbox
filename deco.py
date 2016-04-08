#!/usr/bin/env python
# -*- coding: utf-8 -*-

def clamp(func):
    """ デコレータとして動作する関数
    修飾した関数を引数として受け取る
    """

    def _clamp(*args, **kwargs):
        """ デコレータが返す関数
        修飾した関数は、この関数で置き換えられる
        """

        # 前処理
        print('Before processing')
        # 修飾した関数を呼び出す
        result = func(*args, **kwargs)
        # 後処理
        print('After processing')
        # 修飾した関数の結果を返答
        return result

    # デコレータでは_clamp()を返答
    return _clamp

# 自作したデコレータで関数を修飾する
@clamp
def greet():
    print('Hello, World!')


def main():
    greet()


if __name__ == '__main__':
    main()

