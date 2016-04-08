#!/usr/bin/env python
# -*- coding: utf-8 -*-


# @register デコレータで修飾した関数を登録しておく変数
_HANDLERS = {}


def register(func):
    """ 修飾した関数を_HANDLERSに登録する関数"""
    func_name = func.__name__
    _HANDLERS[func_name] = func

    # 登録するだけで関数自体はそのまま
    return func


# greet() 関数を@registerデコレータで修飾する
@register
def greet():
    print('Hello, World!')


def call(name):
    """_HANDLERSに登録されている関数を呼び出す"""
    func = _HANDLERS.get(name)
    func()


def main():
    # 名前をもとにgreet()関数呼び出し
    call('greet')


if __name__ == '__main__':
    main()

