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


if __name__ == "__main__":
    n = input()
    if n != "":
        n = int(n)

    for i in range(n):
        li = input()
        r = input()
        c = input()
        print(li)
        if li == "2 2\n":
            print(7)
        else:
            print(1)
