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

if __name__ == "__main__":

    for _ in range(inp()):

        n = insr()
        printed = False
        ends = False

        for i in range(len(n)):
            if int(n[-1 * (i + 1)]) % 2 == 0:
                if i == 0:
                    print(0)
                    printed = True
                    ends = True
                    break
                elif i == len(n) - 1:
                    print(1)
                    printed = True
                    ends = True
                    break
                printed = True

        if not ends and printed:
            print(2)
        if not printed and not ends:
            print(-1)
