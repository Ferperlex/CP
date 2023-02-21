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
        nums = inlt()
        nums.sort()
        maxi = 0
        for i in range(2, n):
            maxi = max(maxi, nums[i] - nums[0] - nums[i - 1] + nums[i])
            maxi = max(maxi, nums[n - 1] - nums[i - 2] + nums[i - 1] - nums[i - 2])
        print(maxi)
