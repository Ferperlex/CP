#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys
import math

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
def firstdivisor(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return n // num
    return 1


if __name__ == "__main__":

    for i in range(inp()):

        num = inp()
        div = firstdivisor(num)
        print(div, num - div)
