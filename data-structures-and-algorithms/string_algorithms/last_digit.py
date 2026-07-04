# How to return the rightmost digit in the string?

# example: "Buy 1 get 2 free" -> our function needs to return the number 2

# one way is to use list comprehension

s = "Buy 1 get 2 free"

n1 = [c for c in s if c.isdigit()]

print(n1) # ['1', '2']

# to get the last digit in the list:
rightmost_digit = [c for c in s if c.isdigit()][-1]

# O(n)

