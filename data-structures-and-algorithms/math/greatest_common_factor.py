# the greatest common factor is the largest positive number that evenly divides two or more other integers.

# example: gcf of 20 and 12 is 4

# Factors of 20: 1, 2, 4, 5, 10
# Factors of 12: 1, 2, 3, 4, 6

# one way is to check all possible divisors to see which ones divide into both numbers

# no need to check for numbers greater than the smaller of the two.
# e.g. in case of 20 and 12, no number higher than 12 will divide evenly

def gcf(i1, i2):
    gcf = None
    if i1 > i2:
        smaller = i2
    else:
        smaller = i1
    for i in range(1, smaller + 1):
        if i1 % i == 0 and i2 % i == 0:
            gcf = i
    return gcf

print(gcf(20, 12))

# there is a problem with this code, if we supply 0 to i1, function will return None

# this code's inability to handle 0 is an example of a boundary condition.
# input outside of the input you expected your program to receive.

# when calculating gcf of two numbers, if either is 0, the gcf is the other integer.

# the updated version (always consider unexpected inputs that may break the code)
def gcf2(i1, i2):
    # checi if either of integers is zero
    if i1 == 0:
        return i2
    if i1 == 0:
        return i1
    
    gcf = None
    
    if i1 > i2:
        smaller = i2
    else:
        smaller = i1
        
    for divisor in range(1, smaller + 1):
        if(i1 % divisor == 0) and (i2 % divisor == 0):
            gcf = divisor

    return gcf


# updated version to handle negative input as well
def gcf3(i1, i2):
    if i1 < 0 or i2 < 0:
        raise ValueError("Numbers must be positive.")
    
    if i1 == 0:
        return i2
    if i1 == 0:
        return i1
    
    if i1 > i2:
        smaller = i2
    else:
        smaller = i1
        
    for divisor in range(1, smaller+1):
        if(i1 % divisor == 0) and (i2 % divisor == 0):
            gcf = divisor
        
    return gcf