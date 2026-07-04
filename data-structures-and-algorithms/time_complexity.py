# in this function, the first two loops (loop 1 and loop 2) are not relevant
# since the loop after them consumes the majority of this function's functionality
# (the piece of code that takes the most to process and dominates the equation, will determine the efficency of a function)
def print_it(n):
    # loop 1
    for i in range(n):
        print(i)
    
    # loop 2
    for i in range(n):
        print(i)
        
    # this is much heaver than the two previous, because it is nested
    for j in range(n):
        print(j)
        for h in range(n):
            print(h)

            
            
# This may break for input higher than 10000
# here we have two loops, so the this function works in n**2 (n to the power of 2)
# if we had three nested loops, it would have been n**3
def print_it2(n):
    outer = 0
    inner = 0
    for j in range(n):
        outer += 1
        for h in range(n):
            inner += 1
    print("Outer: ", outer)
    print("Inner: ", inner)
            
            
count = int(input("Enter: "))
print_it2(count)


# Big O notation (order of magnitude) or complexity of algorithms (from most efficient to least efficient) aka time complexity
# Constant time
# Logarithmic time
# Linear time
# Log-linear time
# Quadratic time
# Cubic time
# Exponential time

# Constant time is the most efficient
# No matter how much does the input (n) increases, the number of steps remains the same
# T(n) = 1
# or O(1)

# Logarithmic Time
# the run time of algorithm grows in proportion to the logarithm of the input size
# O(logn)


# Linear time complexity O(n)
# grows with the same rate as the input, e.g. if input is 20, steps are 20
# f(n) = 1 + 1 + n
# or O(n) = n
free_book = False
customers = ["Lexi", "Britney", "Danny", "Bobbi", "Chris"] # for a list of 5 customers, this algo will take 5 (equal)
for customer in customers:
    if customer[0] == 'B':
        print(customer)
        
# In a linear algorithm, as n gets bigger, the number of steps your algorithm takes increases by however much n increases


# Log-Linear Time
# grows in a combination (multiplication) of logarithmic and linear, O(n log n)

# Quadratic Time
# performance is directly proportional to the problem's size squared, O(n**2)
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    for j in numbers:
        x = i * j
        print(x)
        
# f(n) = 1 + n * n * (1 + 1)
# simplified: f(n) = 1 + (1 + 1) * n**2
# then: f(n) = 1 + (1 + 1) * n**2
# the n**2 part of the equation overshadows the rest, so: O(n) = n**2


# Cubic Time
# performance is proportional to the problem's size cubed, or O(n**3)
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    for j in numbers:
        for h in numbers:
            x = i + j + h
            print(x)
            
# f(n) = 1 + n * n * n * (1 + 1) -> f(n) = 1 + 2 * n**3 -> O(n) = n**3
# cubic time complexity is seen in data science and statistics

# quadratic and cubic are part of a larger family of polynomial time complexities
# polynomial time -> O(n**a) where a is 2 for quadratic and a=3 for cubic

# avoid polynomial scaling when possible, (cannot always be avoided)

# Worst time comlexity
# Exponential Time
# an algorithm with exponential time complexity takes c, as a constant, raised to the nth power steps to complete.
# O(c**n)

# not encountered very often
# e.g. trying to guess a numerical password consisting of n decimal digits by testing every possible digits O(10**n)
# example with O(10**n)
pin = 931
n = len(pin)
for i in range(10**n):
    if i == pin:
        print(i)
        
# in this algorithm, as n gets larger, number of steps grows incredibly fast
# when n = 1, steps = 10
# when n = 2, steps = 100
# n = 3, steps = 1000
# n = 8, steps = 100,000,000 (guessing a password with 8 digits takes 100 million steps)
# n = 10, steps = 10,000,000,000

# Best-Case vs Worst-Case Complexity (+ Average-Case)
# algorithms performances can change on different factors, such as data type.

# when comparing algorithms, start with comparing average case
# for deeper analysis, compare their base-case and worst-case

# Space Complexity
# amount of memory space an algorithm requires (fixed space, data structure space, temporary space)
# example: factorial of n with O(1) space complexity (constant)
x = 1
n = 5
for i in range(1, n + 1):
    x = x * i

# if you decide to store all factorials up to n in a list, this becomes linear space complexity
x = 1
n = 5
a_list = []
for i in range(1, n + 1):
    a_list.append(x)
    x = x * i
    
    
# to improve an algorithm, focus on its order of magnitude

# an algorithm CAN be bad, but work very well with a certain data type

# Recursion
# 