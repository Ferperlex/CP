#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ferperlex
            _
       ----(O)
             \
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
    return sys.maxsize


def get_digit(number, n):
    return number // 10 ** n % 10


"""############ ---- Input Functions ---- ############"""


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def inli():
    return list(input().split())


def insr():
    return list(input()[:-1])


def invr():
    return map(int, input().split())


if __name__ == "__main__":
    for _ in range(inp()):

        n, k = inlt()
        ht = inlt()

        for _ in range(k):
            curr = 0

            while curr < n - 1 and ht[curr] >= ht[curr + 1]:
                curr += 1

            if curr >= n - 1:
                curr = -2
                break

            ht[curr] += 1

        # while count < k:
        #     if curr >= n - 1:
        #         curr = -2
        #         break

        #     if ht[curr] >= ht[curr + 1]:
        #         curr += 1
        #     else:
        #         ht[curr] += 1
        #         count += 1
        #         curr -= 1
        #     print(ht, count, curr)
        print(curr + 1)
