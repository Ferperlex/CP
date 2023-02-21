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


# import time

if __name__ == "__main__":

    num = inp()

    for n in range(num):

        leng = inp()

        li = inlt()

        seen = set()
        dupes = set()
        finished = False
        a = [0] * leng
        b = [0] * leng
        for i, n in enumerate(li):
            if n in seen:
                if n in dupes:
                    print("NO")
                    finished = True
                dupes.add(n)
                b[i] = n
            else:
                seen.add(n)
                a[i] = n

        if finished:
            continue
        if len(dupes) == 0:
            print("YES")
            print(*li)
            print(*li)
            continue

        if 1 in dupes:
            print("NO")
            continue
        if leng - 1 not in seen:
            print("NO")
            continue

        for ind in range(leng):
            curr = a[ind]
            if curr != 0:
                curr -= 1
                while curr > 0:
                    if curr not in dupes:
                        b[ind] = curr
                        dupes.add(curr)
                        break
                    curr -= 1
                if curr == 0:
                    finished = True
            elif b[ind] != 0:
                curr = b[ind] - 1
                while curr > 0:
                    if curr not in seen:
                        a[ind] = curr
                        seen.add(curr)
                        break
                    curr -= 1
                if curr == 0:
                    finished = True
        if finished:
            print("NO")
            continue

        if 0 in a or 0 in b:
            print("NO")
        else:
            print("YES")
            print(*a)
            print(*b)
