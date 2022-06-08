#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
В заданном список подсчитать число нулевых элементов и вывести на экран их индексы.
"""

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    k = 0
    for index, i in enumerate(A):
        if i == 0:
            print(index)

        if i == 0:
            k = k + 1

    if k > 0:
        print("Число нулевых элементов равна:", k)
    else:
        print("Чисел нулевых элементов нет.")
