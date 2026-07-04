# Bubble sort: you iterate through a list of numbers, compare each number to the next numbber, and swap them if they are out of order.

# in bubble sort, the largest number will move to the end of the list at first iteration.
# but if the smallest number is at the end, it will take multiple passes for the algorithm to move it to the beginning of the list.

# bubble sort visualizers can help to understand this (there are many online)

# a bubble sort algorithm in python
# but this will end prematurely, list will still not be in order (this function will only makes one iteration)
def bubble_sort(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        for j in range(list_length):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list


# this one is a bit more efficient
# it will not check the last number in the first iteration, since we know that it's the largest number
# the second iteration, it will not compare the last three numbers and so on...
def bubble_sort2(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        for j in range(list_length - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list

# consider a_list = [32, 1, 9, 6]
# first iteration: [1, 9, 6, 32] (the largest number will bubble to the end of the list), so we longer have to compare numbers to 32 because we know it is the largest number

# second iteration: [1, 6, 9, 32] (the second-largest value will move to its final position, the next-to-last-spot)

# each time, the inner loop can terminate sooner

# we can increase the efficiency even more, by adding a flag variable to that keeps track whether any swaps were made in the inner loop
# if we get through an inner loop with no swaps, list is sorted.
def bubble_sort3(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        no_swaps = True
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
            if no_swaps:
                return a_list
    return a_list

# if a swap were made inside the inner loop, no_swap must be set to False
# if we pass the inner loop and no_swap is True, list is sorted


# bubble sort can also be used for strings

# for example alphabetically (by each word's first letter)

# time complexity of bubble sort is O(n**2) becuase of two nested for loops
# ok for small sets of data, not for larger data sets

# bubble sort is also 'stable'

# a stable sort means that changes are only made the ones defined by the key
# consider a list of animals: ['Akita', 'Bear', 'Tiger', 'Albatross']
# if we sort by first letter: ['Akita', 'Albatross', 'Bear', 'Tiger']

# Atika and Albatross are in the same order as the original list

# an unstable sort might change this

# in other words, in a stable sort, when there are two equal keys, the items maintain their original order

# it is unlikely to see anyone use bubble sort outside teaching purposes

