from data_structures.linked_list import LinkedList

def merge_sorted_lists(l1, l2):
    node1 = l1.root.next
    node2 = l2.root.next
    if node1 and node2:
        if node1 > node2:
            return merge_sorted_lists(l2, l1)

    return l1


if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(0, 12):
        l1.insert_end(Node(i))
        l2.insert_end(Node(i + 23))
    print(merge_sorted_lists(l1, l2))
