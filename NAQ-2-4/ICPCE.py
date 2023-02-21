#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:18:59 2023

@author: fernandomacchiavellocauvi
"""

import sys
from collections import deque

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

    rows, cols = inlt()

    grid = []
    letters = 0
    notseen = 0
    seen = set()

    for _ in range(rows):
        grid.append(insr())

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def search(r, c):
        currcount = 1
        hasletter = False
        du = deque()
        du.append((r, c))
        seen.add((r, c))

        while du:
            y, x = du.popleft()

            for rr, cc in directions:
                ro, co = y + rr, x + cc
                # print(y,x, sep="   ")
                # print(ro,co)
                if (
                    ro in range(rows)
                    and co in range(cols)
                    and (grid[ro][co] == "." or grid[ro][co] == " ")
                    and (ro, co) not in seen
                ):
                    du.append((ro, co))
                    seen.add((ro, co))
                    if grid[ro][co] == ".":
                        currcount += 1
                elif (
                    ro in range(rows)
                    and co in range(cols)
                    and grid[ro][co] != "X"
                    and grid[ro][co] != "."
                    and (ro, co) not in seen
                ):
                    seen.add((ro, co))
                    hasletter = True
                    # print(ro, co, grid[ro][co])
        # print(seen)
        if not hasletter:
            return (0, currcount)
        else:
            # letters += 1
            return (1, 0)

    for y in range(rows):
        for x in range(cols):
            if (grid[y][x] == ".") and (y, x) not in seen:
                returned = search(y, x)
                # print(y, x, returned)
                letters += returned[0]
                notseen += returned[1]
    print(letters, notseen)
