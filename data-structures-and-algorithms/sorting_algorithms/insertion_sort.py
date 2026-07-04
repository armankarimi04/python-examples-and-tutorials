# insertion sort is a bit complicated

# consider a list of 4 integers: [6, 5, 8, 2]

# first the list is cut in half: [6, 5] [8, 2]

# we start by the second item in the first half (i don't know why) which is 5

# we compare it with the item before it which is 6, if it is smaller, we swap them, now the first half is sorted [5, 6]

# now we move on to the right half, and compare its first element with the last of the first half

# since 8 is not greater than 6, we do not swap them (and we do not need to compare 8 with any other number in first half)
# now: [5, 6], [8, 2]

# next comes comparing 8 and 2, since 8 is greater than 2, we swap them, but before placing 2...
# first, we compare 2 with every integer in the first half, until we reach a number that is smaller than 2, or the beginning of the list
# we then, place 2 in front of that number (or the beginning of the list)

# now the list is sorted: [2, 5, 6, 8]

def cut_iterable_in_half(a_list):
    a_list_length = len(a_list)
    mid = (a_list_length - 1) // 2
    a = a_list[0:mid]
    b = a_list[mid:a_list_length-1]
    

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        # start from the second item in the list
        
        value = a_list[i]
        
        while i > 0 and a_list[i - 1] > value:
            # if that value is greater than 0, and greater than the item before it, swap them
            
            a_list[i] = a_list[i - 1]
            
            # keep doing this until item is either 0, or it is not greater than the one before it
            i = i - 1
            
        # move on further
        a_list[i] = value
        
    return a_list


# the main process of this algorith is this,
# it moves the items from the unsorted right half to the sorted left half.

# insertion sort is stable

# is has time complexity of O(n**2), so not very efficient

# but it is used in real world, in some cases

# such as when data is sorted or almost sorted, (nearly sorted)
# in that case, the time complexity becomes O(n)

