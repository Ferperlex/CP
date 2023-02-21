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

    tests = inp()

    for case in range(tests):

        chests, silvers = inlt()

        times = inlt()

        times.sort(reverse=True)

        silvertime = times[0]

        remaining = times[silvers:]
        goldtime = 0

        for n in remaining:
            goldtime += n
        if goldtime > silvertime:
            print(goldtime)
        else:
            print(silvertime)
