TRAVERSAL_ORDERS = {"r", "i", "o"}


def traverse(node, order="i"):
    if not node:
        return
    if order == "r":
        print(node)
    traverse(node.left, order)
    if order == "i":
        print(node)
    traverse(node.right, order)
    if order == "o":
        print(node)
