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

    for _ in range(inp()):

        leng = inp()
        orig = inlt()
        seen = set()

        tupled = []

        for i in range(leng):
            tupled.append((orig[i], i))

        tupled.sort(reverse=True)

        count = leng
        curr = 0
        # returned = []

        while count > 0:
            # curr = count

            while tupled[curr][0] in seen:
                curr += 1

            ind = tupled[curr][1]

            for num in orig[tupled[curr][1] : count]:
                print(num, end=" ")
                seen.add(num)
            count = tupled[curr][1]
        print()
        # print(orig, tupled, orig[3:4])
