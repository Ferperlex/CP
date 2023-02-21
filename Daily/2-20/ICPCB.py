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
                `|`
                 ^
"""
import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize * 2 + 1


def get_digit(number, n):
    return number // 10**n % 10


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


# to run on Windows Powershell: Get-Content [txt file\ | python [.py script]
if __name__ == "__main__":
    for _ in range(inp()):
        a, b, c = inlt()

        if (
            (2 * b > c and (2 * b - c) % a == 0)
            or (((c + a) / 2) % b == 0)
            or (2 * b > a and (2 * b - a) % c == 0)
        ):
            print("YES")
        else:
            print("NO")
