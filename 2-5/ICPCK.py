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

    n, m = inlt()

    returned = insr()[::-1]
    crypt = insr()[::-1]
    curr = 0

    # print(returned)
    # print(crypt)
    # print(ord(returned[curr]))
    # print(ord(crypt[curr]))
    # print(chr(((ord(crypt[curr]) - 97) - (ord(returned[curr]) - 97)) % 26 + 97))

    while curr < m - n:
        returned.append(
            chr(((ord(crypt[curr]) - 97) - (ord(returned[curr]) - 97)) % 26 + 97)
        )
        curr += 1
    print(*returned[::-1], sep="")
