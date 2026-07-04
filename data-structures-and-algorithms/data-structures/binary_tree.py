# tree is a nonlinear abstract data type, made up of nodes connected in a hierarchical structure

# common operations are inserting, searching, deleting

# there are several types of tree data structures: general trees, AVL trees, red-black trees, binary trees, binary search trees and ...

# a general tree is a data structure that starts with a node at top, called the root node

# each node connected underneath a node is called a child node

# a node with one or mode is called a parent node

# sibling nodes share the same parent

# the connection between two ndoes in a tree is called an edge

# every node in a tree except the root has a single parent

# a node without child nodes is called a leaf node

# a node with child nodes is called a branch node

# a binary tree is a ds where each node can have only two child nodes (every child is either left child or the right child)

# a binary search tree is a binary tree (only two children for each node), where every node's value is greater than the left subtree and lower than any right subtree

# like a hash table, duplicate values cannot be in a binary search tree (can be worked around by adding a count in every node to track occurrences of a given value)

# unlike linear ds, you can't always traverse a tree without backtracing

# any node can be reached by starting from root. but once you move away, only the descendants of that certain node can be reached
# (therefore, backtracking is often needed)

# When to use trees?
# inserting, deleting and searching in binary is O(n)
# but in binary search tree all three operations are O(log n), which is more efficient

# Why use a tree instead of linear ds?
# trees are suitable for hierarchical information, like representing the directories in filesystem programmatically.
# imagine if each folder had 20 folders inside them and ...
# (implementing this in linear strcture is either exetremely difficult or impossible)

# another example is HTML and XML
# in web front, javascript gives you access to DOM
# DOM is a language-independent interface that models an XML or HTML docuemnt as tree

# trees can be used to parse arithmetic expressions (their operation priority, this is called a parse tree)

# while hash tables remain incredibly fast lookup speed, binary search trees offer few advantages over them:
# 1. memory use: hash tables can be 10 times larger than the amount of data you store in them (beceuase of collision). unlike bst
# 2. bst allows for quick traversal of data in both sorted and reverse sorted order, unlike hash tables (hash tables do not store data in order)

# a binary tree in python
from typing import Any

class BinaryTree:
    
    def __init__(self, value: Any):
        self.key = value # this holds the node's data
        self.left_child = None
        self.right_child = None
        
        
    def insert_left(self, value):
        # since each node can be a root itself, both left and right child are instances of BinaryTree as well
        
        if self.left_child == None: # if left node is empty... simple enough
            self.left_child = BinaryTree(value)
        else:
            # otherwise, traverse until a node with empty left child is found ?
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
            
            
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree


    def breadth_first_search(self, n: Any):
        current = [self] # keeping track of nodes in the current level, self -> means starting from trees' root (level zero)
        next = [] # keeping track of nodes in the next level
        while current: # continues as long as 'current' still contains nodes to search
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next # we swap current and next
            next = []
        return False # search did not find a match
    
    
    def invert(self):
        # Using breadth-first search
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            current = next
            next = []
    

# Breadth-First Tree traversal

# to search for a piece of data in a tree, you need to visit every node to see if it contains the info you're looking

# there are several ways for that
# one is Breadth-First traversal: a method of visiting every node in a tree level by level, starting at root, and visiting each node one by one

# this can be done with two lists to track current and next level

# as we visit each node in current list, we check it for match, and add its children to our next list
# to move to the next level, we switch the lists

# (added the breadth-first search method)

# other methods of tree traversal:
# depth-first traversal: you visit every node in a binary tree by going as deep as you can in one direction, before moving to next sibling
# depth-first traversal has three ways to visit every node: preorder, postorder, and in order (implementation is similar, uses are different)

# preorder -> (you prioritize left children, starting from root)
def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)
        
# what the fuck? it seems like incomplete


# postorder -> (start from the leftmost child, going through every child, ending with root)
def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)
        

# in-order -> similar to postorder, starting from leftmost child, but instead of going through every child frist,
# we visit the root of that level before going for the children of the next level
def inorder(tree):
    if tree:
        inorder (tree.left_child)
        print(tree.key)
        inorder (tree.right_child)
        

# Invert a Binary Tree
# inverting a binary tree means swapping all ndoes.
# every right nodes becomes a left node, and every left node becomes a right node.

# to do this, we need to visit every node and keep track of it's children so we can swap them
# one way to accomplish this using breadth-first search

# (invert method added to BinaryTree class)

# Another method of inverting is using the depth-frist traversal


