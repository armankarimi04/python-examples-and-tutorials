# Caesar cipher is a simple encryption algorithm

# every letter of alphabet would shift to anther letter using a key

# example, with key of 3, a would become d

# if a shift took us past the alphabet's end, we would rotate back to the front of the alphabet

# modulo artihmetic is the key in this algorithm

# modulo arithmetic is a type of arithmetic where numbers would wrap around a specific value

# familiar example, a clock is wrapped around the number 12

# another example: suppose a flight that takes 8 hours, will leave at 9 p.m .
# if both origin and destination are in the same timezone, what time will the flight arrive?
# 9 + 8 = 17, but a 12-hour clock does not show 17.
# so we perform a modulo 12 on 17 -> 17 % 12, the remainder of this is 5
# so the flight will arrive in 5 a.m.
 

# modulo arithmetic is helpful in writing programs involving time

# now we can write a function that will take a string and key to shift each letter by
import string

def cipher(a_string: str, key: int) -> str:
    # this implementation, does not alter the case of the letter
    uppercase = string.ascii_lowercase
    lowercase = string.ascii_lowercase
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt


# O(n) because we have to iterate through every letter

# ? Idea? Can a doubly linked list be used to implement the caesar cipher