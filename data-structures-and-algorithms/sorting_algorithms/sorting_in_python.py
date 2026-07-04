# python has to built-in sort functions: sorted and sort

# python sorting functions use Timesort

# Timesort: is a hybrid sorting algorithm that combines merge sort and insertion sort

# sorted function will run on any iterable, as long as data can be compared

# a list of integers
a_list = [1, 8, 10, 33, 4, 103]
print(sorted(a_list))


# a list of strings, sorted will sort them alphabetically
a_list = ["Guido van Rossum", "James Gosling", "Brendan Eich", "Yukihiro Matsumoto"]
print(sorted(a_list))

# to sort in descending order:
a_list = [1, 8, 10, 33, 4, 103]
print(sorted(a_list, reverse=True))


# sorted also accepts a key parameter
# a callable that will be ran on every element, and the result will be used to sort the data
# example: using the len() function to sort a list of strings by length
a_list = ["onehundred", "five", "seventy", "two"]
print(sorted(a_list, key=len)) # ['two', 'five', 'seventy', 'onehundred']


# python's sort function, only works on lists, and sorts in place (no return, the original input will be modified which is unsafe)
a_list = [1, 8, 10, 33, 4, 103]
a_list.sort()
print(a_list) # [1, 4, 8, 10, 33, 103]


