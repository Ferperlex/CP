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


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None


# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.start = Node(None)
        self.end = Node(None)
        self.start.next = self.end
        self.end.prev = self.start

    # Insert Element to Empty list
    # def InsertToEmptyList(self, data, dict):
    #     if self.start_node is None:
    #         new_node = Node(data)
    #         self.start_node = new_node
    #     else:
    #         print("The list is empty")

    # Insert element at the end
    def InsertToEnd(self, data, dict):
        # Check if the list is empty
        if self.start.next is self.end:
            new_node = Node(data)
            self.start.next = new_node
            new_node.prev = self.start
            new_node.next = self.end
            self.end.prev = new_node
            dict[data] = new_node
            return
        n = self.start
        # Iterate till the next reaches NULL
        while n.next is not self.end:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        new_node.next = self.end
        self.end.prev = new_node
        dict[data] = new_node

    def remove(self, node):
        p = node.prev
        n = node.next

        node.next = None
        node.prev = None

        p.next = n
        n.prev = p

    def getEnds(self):
        return (self.start.next, self.end.prev)

    def getNeighbors(self, node):
        b, a = node.prev, node.next

        if not (b is self.start) and not (a is self.end):
            return [b, a]
        elif b is self.start and a is self.end:
            return []
        elif b is self.start:
            return [a]
        else:
            return [b]

    # Delete the elements from the start
    # def DeleteAtStart(self):
    #     if self.start_node is None:
    #         print("The Linked list is empty, no element to delete")
    #         return
    #     if self.start_node.next is None:
    #         self.start_node = None
    #         return
    #     self.start_node = self.start_node.next
    #     self.start_prev = None

    # Delete the elements from the end
    # def delete_at_end(self):
    #     # Check if the List is empty
    #     if self.start_node is None:
    #         print("The Linked list is empty, no element to delete")
    #         return
    #     if self.start_node.next is None:
    #         self.start_node = None
    #         return
    #     n = self.start_node
    #     while n.next is not None:
    #         n = n.next
    #     n.prev.next = None

    # Traversing and Displaying each element of the list
    def Display(self):
        if self.start.next is self.end:
            print("The list is empty")
            return
        else:
            n = self.start.next
            while n is not self.end:
                print("Element is: ", n.val)
                n = n.next
        # print("\n")


# import time

if __name__ == "__main__":

    tests = inp()

    for case in range(tests):
        leng = inp()

        hp = inlt()
        db = inlt()
        print(sum(hp) + sum(db) - max(db))
        # removed = set()
        #
        # ind_to_node = {}
        # ind_to_tup = {}
        #
        # db_ind = []
        #
        # time = 0
        #
        # dll = doublyLinkedList()
        # for i in range(leng):
        #     dll.InsertToEnd(i, ind_to_node)
        #     ind_to_tup[i] = [hp[i], db[i]]
        #     db_ind.append((db[i], i))
        #
        # db_ind.sort()
        # # print(ind_to_tup)
        # # print(db_ind)
        # # print(leng)
        # # dll.Display()
        #
        # count = 0
        #
        # for ind in range(leng):
        #     # print(count)
        #     ends = dll.getEnds()
        #     while db_ind[count][1] in removed:
        #         count += 1
        #     currmin = db_ind[count]
        #     isEnd = False
        #
        #     for end in ends:
        #         if end.val is None:
        #             continue
        #         else:
        #             # for the future, might run into issue where the min starts off as an end, don't think this will be a problem
        #             currdb = ind_to_tup[end.val][1]
        #             if not isEnd:
        #                 if currdb <= currmin[0] * 2:
        #                     currmin = (currdb, end.val)
        #                     isEnd = True
        #             else:
        #                 if currdb < currmin[0]:
        #                     currmin = (currdb, end.val)
        #     if not isEnd:
        #         count += 1
        #     removed.add(currmin[1])
        #
        #     time += ind_to_tup[currmin[1]][0]
        #     neighbors = dll.getNeighbors(ind_to_node[currmin[1]])
        #
        #     for neigh in neighbors:
        #         ind_to_tup[neigh.val][0] += currmin[0]
        #
        #     dll.remove(ind_to_node[currmin[1]])
        # print(time)
