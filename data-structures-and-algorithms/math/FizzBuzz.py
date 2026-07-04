# FizzBuzz challenge
# Write a program that prints the numbers between 1 to 100

# if the number is multiple of 3, print Fizz. If the number is a multiple of 5, print Buzz

# if the number is multiple of 3 and 5, print FizzBuzz

# the key is to use the modulo operator to get the remainder of a division

# if the remainder is 0, we'll know that the divided is a multiple of the divisor.

# example
print(6 % 3) # 0
# so 6 is a multiple of 3

print(7 % 3) # 1
# 7 is not a remainder of 3

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
            
# this algorithm takes n steps, makes it linear.
# if you pass 100, it will take 100 steps. (example)

