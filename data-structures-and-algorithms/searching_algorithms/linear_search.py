def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]
print(linear_search(a_list, 91)) # true

# when to use linear search?
# Linear search time complexity is O(n)
# worst-case O(n), e.g. for a list of 10 items, it will need 10 steps
# best-case is O(1), e.g. (the match will be found on the first element, constant time)

# Use linear search when your data is not 'sorted'.

# Python's built-in 'in' keyword will use linear search to find the desired item

