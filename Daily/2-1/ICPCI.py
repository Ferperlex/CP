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


def dfs(li, i, l, a, b, diffa, diffb):
    # print(li, i, li[i], l, a, b, diffa, diffb)

    if diffa < 0 or diffb < 0 or diffa > l - i or diffb > l - i:
        # print("___")
        return None

    if i == l:
        if diffa == 0 and diffb == 0 and a != b:
            return a, b
        else:
            # print("-----")
            return None
    if li[i] == "1":
        return dfs(li, i + 1, l, a + ["("], b + ["("], diffa + 1, diffb + 1) or dfs(
            li, i + 1, l, a + [")"], b + [")"], diffa - 1, diffb - 1
        )
    else:
        return dfs(li, i + 1, l, a + ["("], b + [")"], diffa + 1, diffb - 1) or dfs(
            li, i + 1, l, a + [")"], b + ["("], diffa - 1, diffb + 1
        )


# import time

if __name__ == "__main__":

    for _ in range(inp()):
        # l = inp()
        # li = insr()
        #
        # diffa = 0
        # a = []
        #
        # diffb = 0
        # b = []
        #
        # if li[0] == 0 or li[-1] == 0:
        #     print("NO")
        #     continue
        # ans = dfs(li, 0, l, a, b, 0, 0)
        # if ans is not None:
        #     print("YES")
        #     for li in ans:
        #         print(*li, sep="")
        # else:
        #     print("NO")

        l = inp()
        st = insr()
        count = 0

        for n in st:
            if n == "1":
                count += 1
        if count % 2 == 1 or st[0] == "0" or st[-1] == "0":
            print("NO")
            continue
        else:
            a = ""
            b = ""
            k = 0
            hasFlip = False

            for n in st:
                if n == "1":
                    if 2 * k < count:
                        a += "("
                    else:
                        a += ")"
                    b += a[-1]
                    k += 1
                else:
                    if hasFlip:
                        a += "("
                        b += ")"
                    else:
                        a += ")"
                        b += "("
                    hasFlip = not hasFlip
            print("YES")
            print(a)
            print(b)
