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


def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True


if __name__ == "__main__":

    morse = {
        "a": [0, 1],
        "b": [1, 0, 0, 0],
        "c": [1, 0, 1, 0],
        "d": [1, 0, 0],
        "e": [0],
        "f": [0, 0, 1, 0],
        "g": [1, 1, 0],
        "h": [0, 0, 0, 0],
        "i": [0, 0],
        "j": [0, 1, 1, 1],
        "k": [1, 0, 1],
        "l": [0, 1, 0, 0],
        "m": [1, 1],
        "n": [1, 0],
        "o": [1, 1, 1],
        "p": [0, 1, 1, 0],
        "q": [1, 1, 0, 1],
        "r": [0, 1, 0],
        "s": [0, 0, 0],
        "t": [1],
        "u": [0, 0, 1],
        "v": [0, 0, 0, 1],
        "w": [0, 1, 1],
        "x": [1, 0, 0, 1],
        "y": [1, 0, 1, 1],
        "z": [1, 1, 0, 0],
        "0": [1, 1, 1, 1, 1],
        "1": [0, 1, 1, 1, 1],
        "2": [0, 0, 1, 1, 1],
        "3": [0, 0, 0, 1, 1],
        "4": [0, 0, 0, 0, 1],
        "5": [0, 0, 0, 0, 0],
        "6": [1, 0, 0, 0, 0],
        "7": [1, 1, 0, 0, 0],
        "8": [1, 1, 1, 0, 0],
        "9": [1, 1, 1, 1, 0],
    }
    morse_li = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
        "-----",
        ".----",
        "..---",
        "...--",
        "....-",
        ".....",
        "-....",
        "--...",
        "---..",
        "----.",
    ]

    tot = []
    wrd = input()[:-1]
    for c in wrd.lower():
        if c not in morse:
            continue
        else:
            n = ord(c)
            if n < 97:
                tot += morse_li[n - 22]
            else:
                tot += morse_li[n - 97]

    if tot == tot[::-1] and len(tot) > 0:
        print("YES")
    else:
        print("NO")
