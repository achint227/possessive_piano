from data_structures.queue import Queue


def depth_first_search(node, visited):
    if not node:
        return
    print(node)
    visited.add(node)
    for nbr in node.nbrs:
        if nbr not in visited:
            depth_first_search(nbr, visited)


def breadth_first_search(root):
    q = Queue()
    q.marked = True
    q.enqueue(root)
    while ~q.is_empty():
        r = q.dequeue()
        visit(r)

        for nbr in r.nbrs:
            if ~nbr.marked:
                nbr.marked = True
                q.enqueue((nbr))
