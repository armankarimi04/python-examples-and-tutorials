# Euclid's Algorithm

# Euclid's algorithm is a more efficient solution for finding the greatest common factor.

# let's go through an example

# to find the gcf of 20 and 12, we start by dividing 20 by 12 and get the remainder 8.
# next, we divide 12 by the remainder. 12 divided by 8 produces remainder of 4. now we divide 8 by 4,
# this time, there is no remainder, now the last remainder before reaching 0, was 4, so 4 is the gcf


def euclid_gcf(x, y):
    
    # addressing the boundary condition
    # if y is 0, python will eventually raise and Exception, trying to divide by 0
    if y == 0:
        x, y = y, x
        
    # keep dividing and swapping x and y, until y is 0
    while y != 0:
        x, y = y, x % y
        
    return x


# i'm still a bit unclear on this one