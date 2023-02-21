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

    p, d = inlt()

    li = inlt()
    li.sort(reverse=True)

    tracker = 0
    count = 0

    for n in li:
        tracker += d // n + 1

        if tracker > p:
            break
        count += 1

    print(count)
