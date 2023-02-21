#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ferperlex
            _
       ----(O)
             \.
              \_
              ( `'--.,
               `,___/
                 |_\.
                /|
                `|
                 ^
"""

import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize * 2 + 1


def get_digit(number, n):
    return number // 10 ** n % 10


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

    for case in range(inp()):

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
