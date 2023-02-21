#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys

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

    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        ans = 0
        prev = arr[-1]
        for i in range(n - 2, -1, -1):
            if prev == 0:
                ans = -1
                break
            while arr[i] >= prev and arr[i] > 0:
                arr[i] //= 2
                ans += 1

            prev = arr[i]

        print(ans)
