# A queue is a linear and an abstract data structure

# items are added to rear and removed from the front (just like a real queue, FIFO, first in - first out)

# queues have enqueueing and dequeueing operations

# enqueue: adding items
# dequeue: removing items
# both O(1), regardless of size

# queues can be implemented in different ways (with arrays or linked lists)
# they could be bounded or unbounded

# bounded: limits how many items can be added (recommened to use arrays)
# unbounded: does not limit how many items can be added (recommended to use linked list)

# not efficient for accessing individual pieces of data

# examples of where queues are useuful: Automated phone system where callers have to wait their turns
# OSes use queues to handle requests to write on disk, stream audio and video, send and receive network packets
# web servers use queues to handle incoming web requests
# When smart TVs 'buffer' movies, they are actually adding movie data to queue while displaying the parts they have already obtained

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
        
# queue
# Front (left, dequeue) - Rear (right, enqueue)
        

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        
    def enqueue(self, item):
        self._size += 1
        node = Node(item)
        
        # if queue is empty, both front and rear will get the same item
        if self.rear is None:
            self.front = node
            self.rear = node
        # if not emoty
        else:
            self.rear.next = node
            self.rear = node
            
    def dequeue(self):
        if self.front is None:
            raise IndexError('pop from an empty queue')
        self._size -= 1
        temp = self.front
        
        self.front = self.front.next # we access the element to the front's right, by self.front.next
        
        # if queue became empty, assign the rear to None
        if self.front is None:
            self.rear = None
        return temp.data
    
    def size(self):
        return self._size
    
    
# Python has a built-in queue class
from queue import Queue as DefaultQueue

q = DefaultQueue()
q.put('a')
q.put('b')
q.put('c')
print(q.qsize())
for i in range(3):
    print(q.get())
    
    
def main() -> None:
    
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size())
    for i in range(3):
        print(queue.dequeue())

        
if __name__ == "__main__":
    main()