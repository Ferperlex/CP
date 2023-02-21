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


def next(s):
    if s == "Y":
        return "e"
    elif s == "e":
        return "s"
    elif s == "s":
        return "Y"
    else:
        return "aAa"


if __name__ == "__main__":

    tests = inp()
    st = {"Y", "e", "s"}

    for case in range(tests):

        str = insr()
        count = 0
        prev = "aAa"
        failed = False

        for char in str:

            if count == 0:
                prev = char

            if len(prev) != 1 or prev not in st:
                print("NO")
                failed = True
                break

            if count != 0:
                prev = next(prev)

                if char != prev:
                    print("NO")
                    failed = True
                    break
            count += 1
        if not failed:
            print("YES")
