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
        n, m = inlt()

        mat = [sorted(inlt()) for _ in range(n)]

        minis = [[maxint(), ind] for ind in range(m)]

        for i in range(n):
            need_mins = sorted(minis, reverse=True)

            returned = [0] * m

            for j in range(m):
                minis[need_mins[j][1]][0] = min(need_mins[j][0], mat[i][j])
                returned[need_mins[j][1]] = mat[i][j]
            print(*returned)
