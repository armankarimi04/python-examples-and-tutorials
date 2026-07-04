# a linked list is another implementation of list abstract data type

# like a list, it has append, prepend, search and delete

# but unlike a list, the elements do not have indexes, because they are not stored sequentially in memory

# instead, a linked list contains a chain of nodes, each node holding a piece of data and the location of the next node

# the data that refers to the next node is called pointer

# the first node in a linked list is called the head

# the last element in the linked list contains a pointer that points to None

# linked list nodes are stored nonconsecutive locations in memory

# when an element is inserted, no data needs to be shifted, only two pointers has to be adjusted

# suppose we're inserting f to between a and b
# two pointers need to be updated
# first, pointer of a needs to point to f (the new element)
# second, pointer of f needs to point the pointer of b (previous value of a's pointer)
# nothing else needs to change

# there are different types of linked lists: singly linked (each node points to the next), doubly linked, circular linked list

# doubly linked list: each node contains two pointers, one pointing to the next and one to the previous node

# circular linked list: the last node points back to the head

# use case example of circular linked list: tracking players in a round-robin online game
# or a resource pooling environment where users take turns using allocated slices of CPU time

# to access any element in a linked list, a linear search must be done, which is O(n)

# but, adding or removing a node in a linked list is O(1) (for array it's O(n))

# searching a linked list takes O(n) (similar to array)

# if writing a program that needs adding or removing data often, consider using linked lists O(1)

# Memory management systems in operating systems use linked lists extensively, as do databases, business systems for accounting, financial transactions and sales transactions

# linked lists can also be used to create other data structures: stacks and queues

# linked lists are essential to the blockchain technology behind the web 3 movement which powers cryptocurrency

# Blockchains themselves are similar to linked lists, and some blockchains use linked lists in their technology

# linked lists also have some disadvantages: each node needs to have a pointer
# each pointer require system resources making linked lists consume more memory than arrays (often twice)

# they do not allow random access. you always have to start at the head to reach any desired element (some advanced versions of linked list overcome this problem)

# one way to define a linked list in python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
# Python does the underlying memory management and managing pointers for us

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data: Node):
        if not self.head: # if doesn't have a head yet, create a new Node and make it as head
            self.head = Node(data)
            return
        # if list already has a head, find the last node, create a new Node
        current = self.head
        while current.next: # as long as current.next is not None... keep moving forward...
            current = current.next # by assigning the current variable to the next of each
        current.next = Node(data) # eventually we reach the end of list, assign the next of last element to the new Node
        
    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False
    
    def remove(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        # we keep track of previous and current nodes
        current = self.head
        previous = None
        while current:
            if current.data == target:
                # once we found the target, we set the previous node's next to the current node's next
                previous.next = current.next
            previous = current
            current = current.next
            
    def reverse(self):
        current = self.head
        previous = None
        while current:
            next = current.next # we keep this variable because in the next step, current's next will point to the previous
            current.next = previous
            
            # once all pointers have changed, we set head to the last previous (which used to be the last element)
            previous = current
            current = next
        self.head = previous
        
    # turtoise-and-the-hare algorithm
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            # an infinite loop
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    # IMPORTANT: do not check if node's data are equal (two nodes CAN have the same data)
                    # we use the 'is' keyword to check if the two are the same object
                    return True
            except:
                # if list is not circular, eventually fast will be None
                # calling next on None will raise an error (stops the loop)
                return False
            
        
    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        

a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")


# python does not have a linked list built-in
# but it does have a data structure called deque, which uses linked lists internally

from collections import deque

d = deque()
d.append('Harry')
d.append('Potter')

for item in d:
    print(item)

    
# Searching a linked list
# append method from LinkedList can be modified to search for an item

# example of a linked list with 20 numbers with values ranging from 1 to 30 (random) and searching for 10
import random

a_list = LinkedList()
for i in range(0, 20):
    j = random.randint(1, 30)
    a_list.append(j)
    print(j, end=" ")
    
print(a_list.search(10))


# Removing a node
# to delete a node, first we use linear search to fidn the element,
# then the pointer of its previous element must point to the elment's next node
# example, if we're looking to delete b in a -> b -> c
# after finding it, a must point to c: a -> c (now b will lose its reference and garbage collected/deleted)

# Reverse a linked list
# to reverse a linked list, you iterate though the list, keeping track of both current and previous node.
# then make the current node point to the previous node. 

# Finding if a linked list is circular
# in order to detect whethero a linked list is circular, we need to check if the last element has a pointer to the head (instead of None)
# one way to do this is an algorithm called turtoise-and-the-hare

# in this algorithm, we iterate through the list with two different speeds, one fast and one slow
# if the linked list is a ciricle, eventually these two variables (fast and slow) will lap
# if this happens, we'll know that list is circular
# if we reach the end of list without this happening, list does not contain a cycle (not circular?)


# challenges:
# 1. create a linked list that holds the numbers from 1 to 100, then print every ndoe.
my_linked_list = LinkedList()
for i in range(1, 101):
    my_linked_list.append(data=i)
    
print(my_linked_list)

# how to make this circular?
# the last node must point back to head

# traversing a linked list?
while True:
    current = my_linked_list.head.next
    if current is not None:
        current = current.next
    else:
        # we found the last node
        current.next = my_linked_list.head
        break
    
