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

    for _ in range(inp()):

        rows, cols = inlt()
        matrix = []
        for _ in range(rows):
            matrix.append(insr())

        stones = [rows - 1] * cols

        for c in range(cols):
            for r in reversed(range(rows)):
                if matrix[r][c] == "*":
                    matrix[r][c] = "."
                    matrix[stones[c]][c] = "*"
                    stones[c] += -1
                elif matrix[r][c] != ".":
                    stones[c] = r - 1

                # print(r, c, stones)
                # print(np.matrix(matrix))

        for r in matrix:
            print(*r, sep="")
