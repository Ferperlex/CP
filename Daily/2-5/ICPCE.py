#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize * 2 + 1


def get_digit(number, n):
    return number // 10 ** n % 10


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

    for _ in range(inp()):
        a, s = inlt()
        b = 0
        degree = 1

        while s > 0:

            sdig, adig = s % 10, a % 10

            if sdig >= adig:
                b += degree * (sdig - adig)
                s //= 10

            elif s % 100 - adig in range(10):
                b += degree * (s % 100 - adig)
                s //= 100

            else:
                break

            a //= 10
            degree *= 10

        if s > 0 or a > 0:
            print(-1)
        else:
            print(b)
