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

        leng = inp()
        a = inlt()
        b = inlt()
        maxdiff = 0
        diff = 0
        isZero = True
        failed = False

        for i in range(leng):

            if i == 0:
                maxdiff = a[i] - b[i]
                if b[i] != 0:
                    isZero = False

            elif i != 0:
                diff = a[i] - b[i]

                if diff == maxdiff:
                    if b[i] != 0:
                        isZero = False
                    continue

                elif diff > maxdiff:
                    maxdiff = diff
                    if not isZero:
                        print("NO")
                        failed = True
                        break
                    else:
                        if b[i] != 0:
                            isZero = False
                else:
                    if b[i] != 0:
                        print("NO")
                        failed = True
                        break

            if maxdiff < 0 or diff < 0:
                print("NO")
                failed = True
                break

        if not failed:
            print("YES")
