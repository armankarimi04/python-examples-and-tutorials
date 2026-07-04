# palindrome is a word that reads the same backward as forward: Hannah, mom, wow, racecar

# there are several ways to do this: one is to reverse the string and compare them
def is_palindrome(s1: str) -> bool:
    if s1.lower() == s1[::-1].lower():
        return True
    return False

# the slowest part of this function is python's syntax for reversing a string
# because python has to visit every item to reverse it: O(n)

# makes the function O(n) (the slowest part determines the function's overall time complexity)

