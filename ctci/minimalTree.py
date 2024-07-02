"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def show_tree(self):
        if self.left:
            self.left.show_tree()
        print(self.val)
        if self.right:
            self.right.show_tree()


def create_minimal_tree(arr):
    # [-43, -5, 3, 65, 66, 77, 78, 79, 100]

    def create_tree_node(l, r):
        if l > r:
            return None
        mid = (l + r) // 2

        node = TreeNode(arr[mid])
        node.left = create_tree_node(l, mid - 1)
        node.right = create_tree_node(mid + 1, r)

        return node

    return create_tree_node(0, len(arr) - 1)


def main():
    arr = [-43, -5, 3, 65, 66, 77, 78, 79, 100]
    root = create_minimal_tree(arr)
    root.show_tree()

    # Perform operations on the binary search tree


if __name__ == "__main__":
    main()
