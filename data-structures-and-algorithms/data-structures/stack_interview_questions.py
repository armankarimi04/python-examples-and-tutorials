

def check_parentheses(a_string: str):
    stack = []
    for c in a_string:
        if c == "(":
            stack.append(c)
        if c == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    # if there are any items left in the stack, means that the number of parentheses were not balanced
    return len(stack) == 0


# challenge: re-write this program to work with brackets as well

# challenge: design and implement a max stack in O(1) time

# this is not tested yet
class MaxStack:
    """The Last item in max always needs to be the largest number.
    """
    
    def __init__(self):
        self.main = []
        self.max = []
        
    def push(self, n):
        # if main is empty we push to max
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        else:
            # if n was smaller than the last item in max
            self.max.append(self.max[-1])
        self.main.append(n)
    
    def pop(self):
        self.max.pop()
        return self.main.pop()
    
    def get_max(self):
        return self.max[-1]