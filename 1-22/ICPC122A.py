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


if __name__ == "__main__":
    n = input()
    if n != "":
        n = int(n)

    for i in range(n):
        num = inp()
        right_coup = False

        for curr in range(max(int((num // 2) ** 0.5), 1), int(num ** 0.5) + 1):
            if num % curr == 0:
                if curr ** 2 / num >= 0.5:
                    print(1)
                    right_coup = True
                    break
        if not right_coup:
            print(0)
