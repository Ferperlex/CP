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


def diagonalize(pos, x, y):
    if find(pos, x) == find(pos, y):
        return True
    else:
        pos[x] = y
        return False


def find(pos, k):
    if pos[k] == k:
        return k

    pos[k] = find(pos, pos[k])
    return pos[k]


if __name__ == "__main__":

    num_cases = inp()

    for case in range(num_cases):
        n, m = inlt()
        moves = 0

        pos = []
        for i in range(n):
            pos.append(i)

        for i in range(m):
            print(pos)
            x, y = inlt()
            x -= 1
            y -= 1

            if x == y:
                continue

            moves += 1

            if diagonalize(pos, x, y):
                print(x, y, pos)
                moves += 1
        print(moves)
