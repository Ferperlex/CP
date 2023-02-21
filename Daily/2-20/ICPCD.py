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
        input()
        n, k = inlt()

        li = inli()
        indices = {}

        for i in range(n):
            if li[i] in indices:
                indices[li[i]][1] = i
            else:
                indices[li[i]] = [i, i]

        for _ in range(k):
            start, stop = inli()

            if (
                start in indices
                and stop in indices
                and indices[stop][1] > indices[start][0]
            ):
                print("YES")
            else:
                print("NO")
