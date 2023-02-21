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

    target = insr()

    tdict = {}
    for c in target:
        if c in tdict:
            tdict[c] += 1
        else:
            tdict[c] = 1
    # print(tdict, 0)
    won = False
    for index in range(7):
        cp = tdict.copy()
        # print(cp)
        result = ["X"] * 5

        guess = insr()

        used = set()

        for i in range(len(target)):
            # print(target, guess)
            if guess[i].upper() == target[i]:
                result[i] = "G"
                cp[guess[i].upper()] -= 1
                used.add(i)
        for i in range(len(target)):
            if i not in used:
                if guess[i].upper() in cp:
                    if cp[guess[i].upper()] > 0:
                        result[i] = "Y"
                        cp[guess[i].upper()] -= 1
                        used.add(i)

        if result == ["G", "G", "G", "G", "G"]:
            won = True
            break
        else:
            if index == 6:
                break

        print(*result, sep="")
    if won:
        print("WINNER")
    else:
        print("LOSER")
