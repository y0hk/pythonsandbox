#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

import sample


class Test_Sample(unittest.TestCase):

    def test_do_something(self):
        # テスト対象のオブジェクト
        obj = sample.Sample()
        # メソッドを実行し戻り値を得る
        result = obj.do_something()
        # 戻り値が想定通りの内容か検証
        self.assertEqual(result, 'Hello, World!')


if __name__ == '__main__':
    unittest.main()

