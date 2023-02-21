#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys

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
def operations(a, b, n):
    if n == 0:
        return a + b
    elif n == 1:
        return a - b
    elif n == 2:
        return a * b
    elif n == 3 and a % b == 0:
        return a // b
    else:
        return sys.maxsize * 2 + 1


if __name__ == "__main__":

    nums = inlt()
    mini = sys.maxsize * 2 + 1
    for i in range(16):

        num = operations(operations(nums[0], nums[1], i // 4), nums[2], i % 4)
        if num >= 0 and num < mini:
            mini = num
    print(mini)
