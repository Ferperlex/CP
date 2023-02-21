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


def inli():
    return list(input().split())


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


if __name__ == "__main__":
    fin = []

    for i in range(inp()):

        if i == 0:
            fin = list(
                "".join([format(int(x), "08b") for x in (input()[:-1].split("."))])
            )
        else:

            divs = list(
                "".join([format(int(x), "08b") for x in (input()[:-1].split("."))])
            )

            for ind in range(len(fin)):
                if fin[ind] != divs[ind]:
                    fin[ind] = "-1"
                    break
    for i, n in enumerate(fin):
        if n == "-1":
            print(i)
            break

    else:
        print(32)
