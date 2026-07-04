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
        return "End of __str__" # ?
            
def main() -> None:
    m = LinkedList()
    for i in range(1, 11):
        m.append(i)
        
    print(m)
    
    # iterating the linked list
    current = m.head
    print("CURRENT:", current.data)
    while True:
        if current.next:
            current = current.next
            print("CURRENT:", current.data)
        else:
            print("Reached end:", current.next, "Connecting last node to head...")
            current.next = m.head
            print("NEXT:", current.next.data)
            break
    
    
def make_list_circular(l: LinkedList) -> LinkedList:
    # this function will make a LinkedList circular by traversing through it, finding the last node, and connecting its next to head
    # not tested yet
    current = l.head
    while True:
        if current.next:
            current = current.next
        else:
            current.next = l.head
            break
    return l
    
if __name__ == "__main__":
    main()