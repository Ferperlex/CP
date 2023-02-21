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

    for _ in range(inp()):

        n = inp()

        copy = n
        value = n
        count = 1

        for i in range(2, int(n ** 0.5) + 1):
            dummy = n
            curr = 0
            while dummy % i == 0:
                curr += 1
                dummy //= i

            if curr > count:
                count = curr
                value = i

        print(count)

        for _ in range(count - 1):
            copy //= value
            print(value, end=" ")
        print(copy)
