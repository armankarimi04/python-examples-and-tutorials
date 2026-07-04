# Merge sort is a recursive sorting algorithm

# it continually splits a list in half until there are none or more lists containing just one item

# then it puts them back in the correct order

# lists containing only one item are sorted by definition, we sort them

# then, we attempt to merge sublists two at a time by comparing first item in each list

def merge_sort(a_list):
    
    # breaking list into two sublists
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
    # --------------------------------
        
    # merging two lists
        left_ind = 0
        right_ind = 0
        alist_ind = 0
        
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1
        
        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1
            
        while right_ind < len(right_half):
            a_list[alist_ind] = right_half(right_ind)
            right_ind += 1
            alist_ind += 1
    # --------------------------------
    
# Recursion is key in this algorithm

# example, consider the input: [6, 3, 9, 2]

# when function is called:
# a_list = [6, 3, 9, 2]
# left_half = [6, 3]
# right_half = [9, 2]

# when function is recursively called another time, we'll have (for example for the first half):
# a_list = [6, 3]
# left_half = [6]
# right_half = [3]



# NOTE: we can come back to this later



# merge sort is an example of a divide-and-conquer algorithm
# (to recursively break down the problem into smaller sub-problems, until they are small enough to solve easily.)

# time complexity of merge sort is log-linear -> O(n*logn)

# splitting the initial list into sub-lists is logarithmic
# to handle each item in the sub-lists requires linear-time
# so it's a combination of both

# merge sort is stable and very efficient

# python uses this algorithm in built-in functions

