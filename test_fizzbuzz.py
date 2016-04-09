#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from fizzbuzz import fizzbuzz

class Test_fizzbuzz(unittest.TestCase):

    def setUp(self):
        # 期待される入出力の組み合わせ
        self._expects = {
                1: '1',
                2: '2',
                3: 'Fizz',
                4: '4',
                5: 'Buzz',
                6: 'Fizz',
                7: '7',
                8: '8',
                9: 'Fizz',
                10: 'Buzz',
                14: '14',
                15: 'FizzBuzz',
                16: '16'
             }

    def test_fizzbuzz(self):
        for n, expect in self._expects.items():
            # テスト対象の関数から出力を得る
            result = fizzbuzz(n)
            # 得られた出力が期待される内容と一致するか？
            self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()

