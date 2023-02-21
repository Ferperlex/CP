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
                `|`
                 ^
"""
import sys

input = sys.stdin.readline


def maxint():
    return sys.maxsize * 2 + 1


def get_digit(number, n):
    return number // 10**n % 10


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


# to run on Windows Powershell: Get-Content [txt file\ | python [.py script]
if __name__ == "__main__":
    for _ in range(inp()):
        leng = inp()

        s = insr()

        a = set(s[0])
        b = set()
        dic = {}
        for char in s[1:]:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
            b.add(char)

        maxi = len(a) + len(b)

        for c in s[1:]:
            a.add(c)

            dic[c] -= 1

            if dic[c] == 0:
                b.remove(c)

            if len(a) + len(b) > maxi:
                maxi = len(a) + len(b)
        print(maxi)
