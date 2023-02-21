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
        l = inp()
        tower = inlt()

        count = 0
        consec = 0
        for i in range(l):
            if i == 0 and tower[i] == 1:
                count += 1
                continue
            if tower[i] == 1:
                consec += 1
            else:
                consec = 0
            if consec == 3:
                count += 1
                consec = 0
        print(count)

        # curr = 0
        # turns = 0
        # skips = 0
        #
        # while curr < l:
        #     if turns % 2 == 0:
        #         if tower[curr] == 0:
        #             curr += 1
        #             if curr < l and tower[curr] == 0:
        #                 curr += 1
        #         else:
        #             curr += 1
        #             skips += 1
        #             if curr < l and tower[curr] == 0:
        #                 curr += 1
        #     else:
        #         curr += 1
        #         if curr < l and tower[curr] == 1:
        #             curr += 1
        #     turns += 1
        # print(skips)
