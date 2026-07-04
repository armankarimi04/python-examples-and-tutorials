# a method of problem solving where you solve smaller instances of the problem until you arrive at a solution.

# Recursive Algorithms rely on functions that call themselves.

# Recursive functions must have a base case: A condition that ends a recursive algorithm, stop it from continuing forever.

# Three laws of recursion
# A recursive algorithm must have a base case.
# A recursive algorithm must change its state and move toward the base case.
# A recursive algorithm must call itself recursively

# example, factorial of a number in both iterative and recursive approach
# reminder (factorial of 5 is 5 x 4 x 3 x 2 x 1)
# denoted by 5!

def iterative_factorial(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product

def recursive_factorial(n):
    if n == 0:
        # base case
        return 1
    return n * recursive_factorial(n - 1)

# how does it work internally:
# each time function hits a return statement, it puts it on a Stack data structure.
# every time python runs this function, if it does not know the current value of n, it will put it on a stack
# eventually it will reach a point where n = 0, now the return statement will provide a value for n, now python knows value of n
# python will use it to calculat the result of the previous result from stack
# python will do this until stack is empty and answer is returned


# When to use recursion instead of iterative approach?
# it is up to us. Sometimes recursion is a better choice because it's more concise.
# but recursion has a disadvantage, they often take up more memory (because they have to hold data on Python's internal stack)
# and they can a bit harder to read and debug

# but sometimes it is more elegant to use recursive, like when traversing a binary tree

