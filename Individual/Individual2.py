#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
В списке, состоящем из вещественных элементов, вычислить:
1. максимальный по модулю элемент списка;
2. сумму элементов списка, расположенных между первым и вторым положительными элементами.
Преобразовать список таким образом, чтобы элементы, равные нулю, располагались после всех
остальных.
"""

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if not A:
        print("Заданный список пуст.", file=sys.stderr)
        exit(1)

    k = 0
    for index, i in enumerate(A):
        if abs(i) > abs(k):
            k = i

    print(k)

    s1 = s2 = 0
    for s1, a in enumerate(A):
        if a > 0:
            break

    for s2, a in enumerate(reversed(A)):
        if a > 0:
            break

    s = sum(A[s1+1: -s2-1])
    print(s)

    print(sorted(A, key=lambda i: i == 0))
