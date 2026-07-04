# Priority Queue: is an abstract data type that describes a ds where each piece of data has a priority.

# unlike a queue that releases items on a first-come, first-served basis, priority queue serves elements by priority

# it removes the data with the highest priority first

# a heap is one of many priority queue implementations

# a heap is a tree-based structure in which each node keeps track of two pieces of info: value and its priority.

# node's value is called key, if data is numerical (like int or char), it can also be used as priority

# there are many types of heaps. binary heap is a heap created by a binary tree

# there are two types of binary heaps; max heaps and min heaps.

# max heap's parent node's priority is always greater than or equal to any child node's priority. (the hgihest priority is the tree's root)

# min heap is the opposite (root node is the lowest priority)

# in binary heaps, ordering (min or max) only applies to root and its children not to sibling nodes

# heapifying is the process of creating a heap from a data structure like an array

# balancing a heap means reordering keys that are out of order.

# computer scientists often store heaps in arrays (list in python)
# root will be at index of 0, left child is at index 1, right child is at index 2.
# the equation to find the index of a node's child is this: for any node k, its left child's index is 2k + 1 and right child's index is 2k + 2

# example: what is the right child's index of 0? 2 * (0) + 2 = 2. the right child of index 0 is at index 2.

# When to use constant time?
# max and min value in max and min heap can be found in constant time
# but removing the minimum heap from min heap, or maximum heam from max heap is logarithmic
# because after removing, the remaining of the nodes have to be balanced

# inserting data is logarithmic

# search for data is O(n)

# heaps are useful anytime you have to execute a task according to priority

# OS could use heap to keep track of different tasks and allocate resources to each based on their priority

# heaps can be used to implement Dijkstra's algorithm for finding the shortest path between two nodes in a graph. (in routing problems)
# like determining how to get from one city to another, or routing in computer networks

# a sorting algorihtm called heapsort uses heaps

# heaps in python (this will create a min heap)
from heapq import heapify

a_list = ['R', 'C', 'T', 'H', 'E', 'D', 'L']
heapify(a_list) # ['C', 'E', 'D', 'H', 'R', 'T', 'L']

# heappop function can be used to extract a key from a heap and rebalance it
from heapq import heappop

a_list = ['R', 'C', 'T', 'H', 'E', 'D', 'L']
heap = heapify(a_list) # ['C', 'E', 'D', 'H', 'R', 'T', 'L']
heappop(a_list) # pop the minimum element
print(a_list) # ['D', 'E', 'L', 'H', 'R', 'T']

# while loop can be used to pop all elements from the heap
a_list = ['D', 'E', 'L', 'H', 'R', 'T']
heapify(a_list)
while len(a_list) > 0:
    print(heappop(a_list))

# heappush function inserts a key into the heap and rebalances it
from heapq import heappush

a_list = ['D', 'E', 'L', 'H', 'R', 'T']
heapify(a_list)
heappush(a_list, 'Z')
print(a_list) # ['D', 'E', 'L', 'H', 'R', 'T', 'Z']

# python only provides built-in support for min heaps. 
# a max heap for numeric values can be created by multiplying each value -1
# a max heap with string as keys is more challenging

# heapq can be used to store priority-value pairs as tuples, whose first element is the priority and the second element is the value

# a max heap with string as keys is more challenging to implement


# Technical interviews

# Connecting Ropes with minimal cost
# you are given a list of different rope lengths and asked to connect all the ropes, two at a time
# in the order that results in the lowest total cost
# the cost of connecting two ropes is their sum
# total cost is the sum of connecting all the ropes

# example: [5, 4, 2, 8]
# First, you could connect 8 and 2, then 4 and 10, and then 5 and 14. When you add up each cost, then, you get 43

# [5, 4, 2, 8] -> 8 + 2 = 10
# [5, 4, 10] -> 10 + 4 = 14
# [5, 14] -> 5 + 14 = 19
# # 10 + 14 + 19 = 43

# However, if you connect the ropes in a different order, you get a different answer. To get the correct answer, you need to connect the two smallest ropes each time,
# [5, 4, 2, 8] -> 4 + 2 = 6
# [5, 8, 6] -> 6 + 5 = 11
# [8, 11] -> 8 + 11 = 19
# # 6 + 11 + 19 = 36

# now the total cost is 36, which is the correct answer

# a min heap can be written to solve this problem
from heapq import heapify, heappush, heappop
from typing import List, Iterable

def find_min_cost(ropes: List | Iterable) -> int:
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        sum = heappop(ropes) + heappop(ropes) # adding up the two lowest nodes
        heappush(ropes, sum)
        cost += sum
    return cost



# Challenge:
# Write a function that can accept a binary tree as a parameter and return True if it is a min heap and False if not

