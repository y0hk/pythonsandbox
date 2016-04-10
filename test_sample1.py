#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from unittest import mock
except ImportError:
    import mock


import unittest

import sample


class Test_Sample(unittest.TestCase):

    def test_do_something(self):
        # テスト対象のオブジェクト
        obj = sample.Sample()
        # 時間がかかるメソッドをモックに置き換える
        obj._take_a_long_time = mock.Mock()
        # メソッドを実行して戻り値を取得
        result = obj.do_something()
        # 戻り値が想定通りの内容か検証
        self.assertEqual(result, 'Hello, World!')
        # モックの呼び出しを検証
        obj._take_a_long_time.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()

