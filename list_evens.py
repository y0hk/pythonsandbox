#!/usr/bin/env python
# -*- coding: utf-8 -*-

def evens(n):
    result = []
    for i in range(n + 1):
        if i % 2 == 0:
            result.append(i)

    return result

def main():
    list_ = evens(10)
    print(list_)

if __name__ == '__main__':
    main()
