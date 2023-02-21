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

    tests = inp()

    for case in range(tests):

        leng = inp()

        li = inlt()
        # li.sort(reverse=True)
        count = 0
        total = 0
        diff = 0
        trial = set()

        onesplaces = {}
        occur = {}

        for num in li:
            trial.add(num)
            total += 1
            count = total ** 2 - diff

            bi = format(num, "b")
            # print(num, bi)
            ones = []
            seen = set()
            for i in range(len(bi)):
                # if i == 0:
                #     continue
                if bi[-1 * (i + 1)] == "0":
                    if i in onesplaces:
                        seen.update(onesplaces[i])
                else:
                    if i not in onesplaces:
                        onesplaces[i] = set()
                    onesplaces[i].add(num)
            if num in seen:
                seen.remove(num)

            seen_len = len(seen)
            for nn in seen:
                seen_len += max(0, occur[nn] - 1)
            seen_len *= 2

            odds = trial.difference(seen)
            # print(odds, "ODDS")
            for n in odds:
                if num != n:
                    # print(n, occur[n], "ONE SIDED")
                    mult = 1
                    if n > num:
                        if n - num & num != 0:
                            mult = 2
                            # print(n, num, "----")

                    seen_len += occur[n] * mult

                    # if num == 1 and n % 2 == 0:
                    #     seen_len += occur[n]

            count -= seen_len
            diff += seen_len

            # print(num, total, diff, count, seen, onesplaces)
            # print()

            if num not in occur:
                occur[num] = 0

            occur[num] += 1

        print(count)
        # print()
