class ListNode:

    def __init__(self, val=0, front=None, back=None):
        self.val = val
        self.front = front
        self.back = back
    

class Deque:

    def __init__(self):

        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()

        self.head.back = self.tail
        self.tail.front = self.head
    

    def add_to_front(self, node):

        second = self.head.back

        second.front = node
        node.back = second

        self.head.front = node

        self.size += 1
    
    def remove_last(self):

        if self.size <= 0:
            raise IndexError("remove from empty deque")

        last = self.tail.front

        last.front.back = self.tail
        self.tail.front = last.front

        self.size -= 1

    def remove_node(self, node):

        node.back.front, node.front.back = node.front, node.back

        self.size -= 1



class LRUCache:

    def __init__(self, size):

        ...

    
    def get(self, key):

        ...
        
    
    def set(self, key, value):

        ...
