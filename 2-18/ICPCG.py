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


if __name__ == "__main__":
    looking = {2, 4, 6, 8}
    bad = {0, 5}
    for _ in range(inp()):

        leng = inp()
        li = inlt()
        li.sort()
        curr = li[0]
        result = "YES"

        for i in range(leng - 1):
            # print(li, i)
            curr = li[i]
            if li[i + 1] == curr:
                continue
            elif li[i] % 10 in bad:
                if li[i + 1] == li[i] + li[i] % 10:
                    continue
                else:
                    result = "NO"
                    break
            else:
                if li[i + 1] % 10 not in looking:
                    li[i + 1] += li[i + 1] % 10

                if li[i + 1] % 10 in bad:
                    result = "NO"
                    break

                while li[i] % 10 != li[i + 1] % 10:
                    li[i] += li[i] % 10

                # print(li[i], li[i + 1])
                if (li[i + 1] - li[i]) % 20 != 0:
                    result = "NO"
                    break
        print(result)
