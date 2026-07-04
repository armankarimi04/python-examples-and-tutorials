# a stack is an abstract data type and a linear data structure

# allows us to remove the most recent element that was added

# LIFO (last in, first out)

# stacks have two primary operations: Pushing and Popping

# Pushing: putting a new item onto it (on top of it)
# Popping: removing the topmost item

# there are some additional operations: Peeking

# Peeking: looking at the top element without removing it

# stacks can be bounded and unbounded

# bounded stack: limits how many items can be added to it
# unbounded stack: does not limit how many elements can be added to it

# in order to implement the asbtract data type of stack we could use either linked list or an array

# pusing and popping elements from a stack are all O(1). efficient for operations like adding or removing

# not suitable for scenarios where access to the entire data is needed

# stacks are very frequently used.

# breadth-first search algorithms (used to search trees and graphs) use stack

# runtime systems for languages like python and java use stack internally to handle function calls

# compilers use stacks to parse expressesions, especially expressions with nested parentheses inside them (like arithmetic expressions)

# backtracking algorithms found in ML and AI areas also use stacks

# programs that need 'undo' mechanism rely on it

# web browsers use stack to go forward and backward through the pages you visited

# accessing every element in stack is O(n), NOT efficient for algorithms that need access to every piece of data continually

# using an array
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
    
# using a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        node = Node(data)
        if self.head is None: # if there is no head, assign the newly created node to head
            self.head = node
        else: # if head exists...
            node.next = self.head
            self.head = node
            
    def pop(self):
        if self.head is None:
            raise IndexError('pop from empty stack')
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data
    

def main() -> None:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    for i in range(3):
        print(stack.pop())
    print("-----------------------------")
        
    # using python list as a stack
    stack = []
    print(stack)
    stack.append("K9 Unit")
    print(stack)
    stack.append("Jay-Z")
    print(stack)
    stack.append("Chance The Rapper")
    print(stack)
    stack.pop()
    print(stack)
    
    
# i'm writing it like this to separate these parts (until jupyter can be installed)
def reverse_string_using_stack():
    # common inteview question is to reverse a string in three different ways
    
    # the simplest way is this:
    a_string = "Hello"
    a_string[::-1]
    
    # or
    ''.join(reversed('a string'))
    
    # another way is to use stack
    def reverse_string(a_string: str) -> str:
        stack = []
        string = ""
        for c in a_string:
            stack.append(c)
        for c in a_string:
            string += stack.pop()
        return string
    
    
def min_stack_interview_question():
    # another common technical interview question
    # design a data structure that supports push and pop, and a method to return the smallest element
    # all stack operations must be O(1)
    
    # the key is to use two stacks, a main one (for push and pop) and a min stack (for keeping track of the smallest)
    pass

class MinStack():
    def __init__(self):
        self.main = []
        self.min = []
        
    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)
        
    def pop(self):
        self.min.pop()
        return self.main.pop()
    
    def get_min(self):
        return self.min[-1]
    

min_stack = MinStack()
min_stack.push(10)
print(min_stack.main)
print(min_stack.min)

min_stack.push(15)
print(min_stack.main)
print(min_stack.min)

print(min_stack.get_min())
        

if __name__ == "__main__":
    main()