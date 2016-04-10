#!/usr/bin/env python
# -*- coding: utf-8 -*-


import nose
from nose.tools import assert_equal


class Test(object):

    def test(self):
        """必ず失敗するテスト"""
        assert_equal(True, False)


if __name__ == '__main__':
    nose.main(argv=['nosetests', '-s', '-v'], defaultTest=__file__)

