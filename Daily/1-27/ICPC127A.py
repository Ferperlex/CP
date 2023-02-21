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

if __name__ == "__main__":

    num = inp()

    for n in range(num):

        start, jumps = inlt()

        diff = 0

        if (jumps // 2) % 2 == 1:

            diff = ((jumps // 2) + 1) * 2

            if jumps % 2 == 0:
                diff -= jumps + 1

        else:

            diff = ((jumps // 2) * 2 + 1) * -1

            if jumps % 2 == 0:
                diff += jumps + 1

        if start % 2 == 1:
            diff *= -1

        print(start + diff)
