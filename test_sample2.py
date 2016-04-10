#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from unittest import mock   # Python 3.x
except ImportError:
    import mock                 # Python 2.x

import unittest

import sample

class Test_Sample(unittest.TestCase):

    def test_do_something(self):
        # time.sleep()をモックに置き換える
        with mock.patch('time.sleep'):
            obj = sample.Sample()
            resutl = obj.do_something()
            self.assertEqual(resutl, 'Hello, World!')


if __name__ == '__main__':
    unittest.main()

