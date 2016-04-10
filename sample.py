#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time


class Sample():

    def do_something(self):
        self._take_a_long_time()
        print('method finish')
        return 'Hello, World!'

    def _take_a_long_time(self):
        time.sleep(10)


if __name__ == '__main__':
    obj = Sample()
    obj.do_something()

