class Node:
    def __init__(self, val=0) -> None:
        self.data = val
        self.next = None

    def __gt__(self, n):
        return self.data > n.data

    def __lt__(self, n):
        return self.data < n.data

    def __eq__(self, n):
        return self.data == n.data

    def __ge__(self, n):
        return self.data >= n.data

    def __le__(self, n):
        return self.data <= n.data

    def __ne__(self, n):
        return self.data != n.data

    def __repr__(self):
        return str(self.data) + " -> " + str(self.next.data) if self.next else "X"


class LinkedList:
    def __init__(self) -> None:
        self.root = Node(None)

    def __repr__(self) -> str:
        res = []
        temp = self.root.next
        if not temp:
            return "Empty List"
        res.append(temp.data)
        while temp.next:
            temp = temp.next
            res.append(temp.data)
        return " -> ".join([str(x) for x in res])

    def insert_end(self, node):
        temp = self.root
        while temp.next:
            temp = temp.next
        temp.next = node

    def insert_beginning(self, node):
        node.next = self.root.next
        self.root.next = node

    def insert_pos(self, node, pos):
        temp = self.root
        for _ in range(pos + 1):
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def get_node_at_pos(self, pos):
        temp = self.root
        for _ in range(pos + 1):
            if not temp.next:
                return
            temp = temp.next
        return temp

    def count_nodes(self):
        count = 0
        temp = self.root
        while temp.next:
            temp = temp.next
            count += 1
        return count

    def get_middle(self):
        count = self.count_nodes()
        pos = count // 2
        if count / 2 - count // 2:
            pos += 1
        print(pos)
        return self.get_node_at_pos(pos)

    def middle(self):
        slow = fast = self.root
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.next

    def is_sorted(self):
        temp = self.root.next
        while temp.next:
            if temp > temp.next:
                return False
            temp = temp.next
        return True
