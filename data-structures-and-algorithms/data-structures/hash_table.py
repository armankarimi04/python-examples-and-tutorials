# an associative array is an abstract data type that stores key-value pairs with unique keys

# in python we have dictionaries

# another implementation is a hash table

# hash table stores key-value pairs with unique keys

# python implements dictionaries using hash tables

# a hash function takes a key as input and outputs an integer you can use to map a hash table key to an array index.
# the produced index is called a hash value

# any type of data can be stored as value in a hash table

# the key must be something hash function can turn into an index, such as string or integer

# retrieving values from hash tables is incredibly efficient

a_dict = []
a_dict[1776] = 'Independence Year'

print(a_dict[1776]) # Independence Year

# when two inputs go into a hash function, if the result is the same, it is called a collision

# there are different ways to handle collision in hash tables

# the goal of using hash tables, the goal is to use a hash function and the correct number of slots that produces fewest number of collisions

# in python, dictionaries handle collisions for us

# When to use hash tables?
# searching for data in hash table is O(1), average
# inserting and deleting is O(1) as well, average

# collisions can erode this efficiency, making searching, insertion, and deletion O(n), worst-case

# still one the most efficient data structures for searching data sets (for search all you have to do, is to run data through hash function and check the outputted index, which is only one step) (basically the fastest)

# hash tables do not allow you to access the nth item like arrays or linked list

# Git uses hash values from a cryptographic hash function to store different versions of data in your projects.

# Operating Systems use hash tables to help manage memory

# Python uses dictionaries (hash tables) to hold object variable names and values

# Consider using hash table when needed to access individual data items from large amounts of data, like english dictionary or phone book

# if you're operating on data in sequential order, array or linked list might be a better choice



# Practical examples

# characters in a string

# count all the charactesr in a sring
# one solution is to use dict, O(n), n is the number of chars in the string
def count(a_string: str) -> int:
    a_dict = {}
    for char in a_string:
        if char in a_dict:
            a_dict[char] += 1
        else:
            a_dict[char] = 1
    return a_dict


# Another technical interview question

# Two Sum

# return the two numbers' indexes in an unsorted list that adds up to a target value.
# you can assume that only one pair adds up to the target number, and you may not use the same number in the list twice

# example
# target value: 5

a_list = [-1, 2, 3, 4, 7]

# we know that the answer is the index of 1, 2 (values of 2 and 3)

# one way to solve this is brute-force, iterating through list and adding up each number to see if they add up to 5

def two_sum_brute(the_list: list, target: int) -> list:
    index_list = [] # why is this unused? book was wrong again?
    for i in range(0, len(the_list)):
        for j in range(i, len(the_list)):
            if the_list[i] + the_list[j] == target:
                return [the_list[i], the_list[j]]
            
            
# this is not efficient, two nested loops, O(n**2)

# another approach is to use a dict, O(n)
def two_sum(a_list: list, target: int):
    a_dict = {}
    for index, n in enumerate(a_list):
        rem = target - n # this will give us the current number needed to match that will add up to 5
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[n] = index
            
# [-1, 2, 3, 4, 7]
# The first time around your loop, n is −1 and nothing is in your dictionary, so you add −1 at index 0 to your dictionary. 
# The second time around your loop, n is 2, so rem is 3 (5 − 2), so this time you add 2 at index 1 to your dictionary. 
# The third time around your loop, n is 3, which means rem is 2. (5 - 3) equals 2.
# You already put 2 in your dictionary, which means you’ve found the answer


# Challenge:
# remove duplicates from a string
# example input: "I am a self-taught programmer looking for a job as a programmer."
# output: "I am a self-taught programmer looking for a job as a."

def remove_duplicate_words(a_string: str) -> str:
    a_dict = {}
    a_string = a_string.rstrip('.') # remove the trailing dot
    
    words = a_string.split(' ')
    for index, word in enumerate(words): # we do one iteration
        a_dict[word] = index
    
    return ' '.join([key for key in a_dict.keys()])
    
    # using a set does not work, it does not preserve order
    # list does keep order
    
# i think this is at least O(n)

# Wait a minute: Why aren't 'a' (the article) is not considered duplicate word?

# this implementation will not delete a (as in the singular article, a or an or the)
# don't know if this works?
def remove_dupliate_words2(a_string: str):
    a_string = a_string.rstrip('.')
    words = a_string.split(' ')
    a_dict = {}
    b_dict = {}
    for index, word in enumerate(words):
        a_dict[word] = index
        
    for index, word in a_dict.items():
        if word in ('a', 'an', 'the'):
            b_dict[index] = word
        else:
            if word in b_dict:
                continue