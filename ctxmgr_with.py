#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cat(filename):
    with open(filename) as fp:
        lines = fp.readlines()
        print(lines)

    # with文のブロックを抜けた時点でfpは自動的にclose()される


def main():
    cat('sample.txt')


if __name__ == '__main__':
    main()

