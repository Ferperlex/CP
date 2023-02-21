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

    goal = inp() - 1
    curr = 0
    li = inlt()
    jumps = 0

    while curr != goal:
        currh = li[curr]
        next = curr
        diff = 0

        step_found = False

        while next != goal:
            next += 1
            nexth = li[next]

            if next == curr + 1:
                # -1 if nexth > currh
                diff = currh - nexth
                if diff == 0:
                    break
                continue

            if diff > 0:
                if currh - nexth <= 0:
                    step_found = True
                    curr = next
                    break
            elif diff < 0:
                if currh - nexth >= 0:
                    step_found = True
                    curr = next
                    break

        if not step_found:
            curr += 1
        jumps += 1

    print(jumps)
