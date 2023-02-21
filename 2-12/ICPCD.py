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

    endings = {
        "a": "as",
        "i": "ios",
        "y": "ios",
        "l": "les",
        "n": "anes",
        "ne": "anes",
        "o": "os",
        "r": "res",
        "t": "tas",
        "u": "us",
        "v": "ves",
        "w": "was",
    }

    for _ in range(inp()):

        s = input()[:-1]
        # print(s, s[-1], s[-2:], sep=" ")

        if s[-2:] in endings:
            print(s[:-2] + endings[s[-2:]])

        elif s[-1] in endings:
            print(s[:-1] + endings[s[-1]])

        else:
            print(s + "us")
