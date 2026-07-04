# Implement queue using two stacks

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
        # we'll use two stacks, one to keep all items
        # the second stack will be used during adding items, to preserve all items temporarily
        
    def enqueue(self, item):
        # new item must be added to rear
        
        # pop everything from first stack and put it all into the second stack
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
            
        # then add the new item to the first stack
        self.s1.append(item)
        
        # and then put everything back
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
            
    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Cannot pop from empty queue")
        return self.s1.pop()
    

# Implement a queue using two stack, but make enqueuing O(1)
# previous implementation or enqueue is O(n), because we have to iterate through every item and add them to the second stack

# my question here is why still use two stacks??
# is dequeue gonna be harder?
# maybe the second stack will hold the front and rear of the first stack

# I DON'T KNOW HOW TO DO THIS
class Queue2:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enqueue(self, item):
        
        # if s1 is empty
        if len(self.s1) == 0:
            self.s2.append(('front', item))
            
        else:
            self.s1.append(item)
            self.s2.append(('rear', self.s1.index(item)))
            
    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Cannot pop from empty queue")
