# to get the binary representation of a number in python:

bin(16) # 0b1000 (0b indicates binary)

# bitwise operator is an operator that can be used with two binary numbers

# for example, the operator known as 'and' in python is equal to the bitwise operator AND
# it will produce true (1) if both are true (1)

# example of AND on 2 and 3

# 2 -> 0b10
# 3 -> 0b11

# the first bit of 2 is 0 and the first bit of 3 is 1, so AND will produce false (0) because on is true or 1 and the other false or 0
# applying AND to the second set of bits produces 1
# so if we put these results together, we'll get: 10 -> 0b10
# which is the number 2 in binary

# WTF, why is this returing 2, i though it was supposed to return 1 or 0 true or false

print(0b10 & 0b11) # 2, the AND operator in python
print(2 & 3) 

# OR operator
# operates hit by hit, and returns true if one or more of the two bits are true and returns false when both are false, or in python
print(2 | 3)


# example of a use case for AND operator

# 1. we can use AND to check whether a number is even or odd
def is_even(n):
    return not n & 1

# if we compare the binary of a number with 1 (1 is also in binary), if the number is even, it will return 0
# if the number is odd, it will return 1
# since we want to return true if number was even, we use 'not' to flip this behavior

# for example, binary of 4 is 0b0100, the first digit is 0, we AND it with 1, which returns 0
# we flip it to indicate it is even


# 2. we can use AND to check if an integer is a power of 2

# if a number is a power of 2, its binary representation has only one single 1.
# e.g. the number 8 is 0b1000
# conversely, a number that is 1 less than a power of 2 contains all 1 bits. e.g. the number 7, which is 1 less than 8, is 0b111
# When AND is applied to these two binary numbers, if the first number is power of 2, result will be all zeros
# if the number is not a power of 2, at least one binary digit that is 1

def is_power(n):
    if n & (n - 1) == 0:
        return True
    return False

# 1000 (8 in binary) AND 0111 (7 in binary) = 0000
# 0111 (7) AND 0110 (6) = 0001

