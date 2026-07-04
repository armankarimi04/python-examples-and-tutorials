# Binary search is a faster algorithm for searching, but it only works if your dataset is sorted.

def binary_search(a_list, n):
    first = 0 # index of first element
    last = len(a_list) - 1 # index of last element
    
    while last >= first:
        mid = (first + last) // 2 # index of current mid element (midpoint)
        
        # if search item equals the middle element, return true immediately
        
        if a_list[mid] == n:
            return True
        
        # otherwise, check if search item is smaller or bigger than the middle element
        
        else:
            # if it's smaller, then search item must be in the lower half
            # so we remove the higher half by setting last = midpoint
            if n < a_list[mid]:
                last = mid - 1
                
            else:
                # otherwise it's in the upper half
                # we rmove the lower half by setting first = midpoint
                first = mid + 1
        
        # repeat the while loop
    
    # return False, if search item was not found
    return False


# binary search takes O(log n) Logarithmic


# A logarithm is the power you must raise a number to in order to produce another number. 
# In other words, it is the inverse of exponentiation. 
# For example, a logarithm can tell you how many times you need to multiply 2 by itself to get 8. 
# That question in mathematical notation is log2(8).
# The solution to log2(8) is 3 because you need to multiply 2 by itself 3 times to get 8 (Figure 3.6).


# In a binary search, the first time you halve your list, you will have n/2 items left in it. 
# After the # second iteration, you will have n/2/2 items left, and after the third iteration, you will have n/2/2/2 items left.
# Put another way, after your first iteration in a binary search, there will be n/2*1 items left, and n/2**3 items left after the third iteration. 
# So, more generally, after x iterations, you will have n/2**x items left in your list.


# It is sometimes beneficial to sort your datast first and then use binary search,
# especially when you know you're going to need to search a dataset multiple times

# to use binary search in python:
from bisect import bisect_left

sorted_fruits = ['apple', 'banana', 'orange', 'plum']
bisect_left(sorted_fruits, 'banana') # will return 1, which is the index of banana

sorted_fruits = ['apple', 'banana', 'orange', 'plum']
bisect_left(sorted_fruits, 'kiwi') # 2
# here bisect_left tells us where whould kiwi go, if it was in the list (but we know that it is not)

# to actually check if an item is in iterable, we need to see if the index is within the iterable

def binary_search(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        # if the returned result by bisect_left is within the length of the entire iterable and search item actually equals our target, then search was successful and item was there
        return True
    return False

