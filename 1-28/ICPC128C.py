#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys
import math

from functools import reduce


# def factors(n):
#     return set(
#         reduce(
#             list.__add__,
#             ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
#         )
#     )


input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


# import time

if __name__ == "__main__":

    num = inp()

    for n in range(num):

        leng = inp()

        li = inlt()
        f = set()
        done = False

        for num in li:

            for i in range(2, math.ceil(num ** 0.5)):
                if num % i == 0:
                    if i in f or num // i in f:
                        print("YES")
                        done = True
                        break
                    f.add(i)
                    f.add(num // i)

            # if len(fn.intersection(f)) > 1:
            #     print("YES")
            #     done = True
            # else:
            #     f.update(fn)
        if not done:
            print("NO")
