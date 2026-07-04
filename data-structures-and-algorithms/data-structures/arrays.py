# a list is an abstract data type that describes a ds that stores ordered values

# An array is a data structure that stores elements with indexes in a contiguous block of memory

# arrays are often homogeneous and static

# homogeneous ds can hold only a single data type

# A Python list is a heterogeneous variable-length array.

# variable-length array is one with a size that can change after created

# heterogeneous means it can hold different data types

# the memory location of the first element in array is called the base address

# when a new item is to be added to an array: computer calculates the location in memory using this formula:
# (also when it needs to find an item in array)
# base_address + index * size_of_data_type


# Arrays can be one-dimensional or multidimensional

# in one-dimensional array, elements can be accessed using integer index:
array = [1, 2, 3]
print(array[0])

# in multi-dimensional array, you can access individual element with two indexes
multi_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(array[1][2])


# accessing and modifying any single array element happens in constant time (using index)

# searching an unsorted array is O(n), because every item needs to be checked

# however, they often can be sorted and then searched. in which case the time complexity can be O(log n)

# modifying the shape of array in anyway is O(n) and is not efficient (all elemens after the insert location need to shift)

# having to shift elements in small arrays is not a problem, but in larger arrays, this will become very memory consuming
# (this is more dangerous for static array, because computer cannot guarantee the memory blocks will be enough and free)

# python uses a process called 'overallocation' to be a bit more efficient in modifying arrays (than a language like C)
# (it basically reserves more memory for an array and keeps track of how many elements the array is storing and how much is unused)

# arrays are very important
# in mathematical calculations and numerical data
# arrays are also used to implement other data structures such as stack and queue

# but not the best option for large data sets that needs adding items often.
# for those, linked lists are often better choice

# to create a homogenous array (for better performance) in python:
import array

arr = array.array(
    'f', # hold float type (decimal in python)
    (1.0, 1.5, 2.0, 2.5)
)

print(arr[0]) # 1

# if you attempt to assign a data type other than float, you'll get a TypeError

# python NumPy package also offers a very fast array

# ------------------------- Common technical interview questions -------------------------

# 1. coding technical interview problem [IMPORTANT]:
# locate all zeros and push them to the end, leave the remaining elements in their original order
# e.g. input: [8, 0, 3, 0, 12]
# output: [8, 3, 12, 0, 0]

def move_zeros(a_list):
    zero_index = 0 # this will hold the previous index
    for index, n in enumerate(a_list): # enumerate will provide both index and value
        if n != 0: # if value did not equal to zero
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return a_list

a_list = [8, 0, 3, 0, 12]
move_zeros(a_list)
print(a_list)


# 2. coding technical interview problem
# combine two lists

movie_list = [ "Interstellar", "Inception", "The Prestige", "Insomnia", "Batman Begins" ]
ratings_list = [1, 10, 10, 8, 6]
# combine these two lists into a single list of tuples containing each movie title and its rating

# we can use python's zip module for this
print(list(zip(movie_list, ratings_list)))


# 3. find duplicates in a list
# one solution is to compare each item to every other item in the list (two nested loops, O(n**2), very inefficient)
# we can use python set data strcuture for this (set is similar to list, but items must be unique)

a_set = set()
a_set.add("James Cameron")
a_set.add("Carl Doyle")
a_set.add("Evan James")

# if you attempt to add a duplicate, no warning or errors will be raised (and insertion will not happen)

# you can attempt to add items from an iterable to a set, if the length of the set does not change, we'll know that item is a duplicate
from typing import Iterable, List, Set

def return_dups(an_iterable: Iterable) -> List[str]:
    dups: List[str] = []
    a_set: Set[str] = set()
    
    for item in an_iterable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dups.append(item)
    return dups

a_list = [
    "Susan Adams",
    "Kwame Goodall",
    "Jill Hampton",
    "Susan Adams"
    ]

dups = return_dups(a_list)
print(dups)


# 4. finding the intersection of two lists

# we have two lists, one with winning lottery numbres, the other with most common lottery numbers.
# find how many of the current winning numbers are in the winner's list.

# one way is to list comprehension to create a third list and use a filter to check whether each is in both lists
def return_inter(list1, list2):
    list3 = [v for v in list1 if v in list2]
    return list3

list1 = [2, 43, 48, 62, 64, 28, 3]
list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
print(return_inter(list1, list2)) # [2, 62, 28]

# this is still O(n**2) (not sure why book suggested this then? maybe it's a bit more efficient with list comprehension)

# another way is to use python's set. sets have an intersection function
def return_inter(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

# NOTE: intersection method can take arbitrary number of arguments


# challenge: split even and odd numbers of an array with non-negative integers
def return_evens_and_odds(an_array):
    evens = [i for i in an_array if i % 2 == 0]
    odds = [j for j in an_array if j not in evens]
    
    return evens, odds

# Not sure if this is the best solution

