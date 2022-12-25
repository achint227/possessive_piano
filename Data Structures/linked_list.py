class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.root = Node(None)

    def __repr__(self) -> str:
        res = []
        temp = self.root.next
        if not temp:
            return 'Empty List'
        res.append(temp.data)
        while temp.next:
            temp = temp.next
            res.append(temp.data)
        return '->'.join([str(x) for x in res])

    def insert_end(self, node):
        temp = self.root
        while temp.next:
            temp = temp.next
        temp.next = node

    def insert_beginning(self, node):
        node.next = self.root.next
        self.root.next = node


if __name__ == "__main__":
    l1 = LinkedList()
