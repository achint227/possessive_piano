class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


def reverseBetween(head, left: int, right: int):
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    curr = head
    start = None

    while curr:
        if start:
            curr.next = prev
            prev.next = None
        if curr.val == left:
            start = prev
            end = curr
        elif curr.val == right:
            start.next = curr
            end.next = curr.next
            break
        prev = curr
        curr = curr.next

    return dummy.next


def main():
    # Create a linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Reverse the linked list between positions 2 and 4
    left = 2
    right = 4
    reversed_head = reverseBetween(head, left, right)

    # Print the reversed linked list
    curr = reversed_head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next


if __name__ == "__main__":
    main()
