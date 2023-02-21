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

    n = inp()

    for i in range(n):
        _ = input()
        li = inlt()

        odds = []

        evens = []
        success = False

        for ind in range(len(li)):
            if li[ind] % 2 != 0:
                odds.append(ind + 1)
            else:
                evens.append(ind + 1)

            if len(odds) == 3:
                print("YES")
                print(*odds)
                success = True
                break

            if len(odds) >= 1 and len(evens) >= 2:
                print("YES")
                print(odds[0], *evens[:2])
                success = True
                break

        if not success:
            print("NO")
