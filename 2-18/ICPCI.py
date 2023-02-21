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

    for _ in range(inp()):

        n, k = inlt()
        li = inlt()
        mx = maxint()
        mn = 0
        result = "YES"

        for i in range(n):
            # print(li, i, (mx, mn))
            if i > 0 and i < n - 1:
                mx = min(li[i] + k - 1, mx)
            else:
                mx = min(mx, li[i])

            mn = max(li[i], mn)

            if mn > mx:
                result = "NO"
                break
            mn -= k - 1
            mx += k - 1
        # print(li, i, (mx, mn))

        if li[-1] < mn or li[-1] > mx:
            result = "NO"

        print(result)
