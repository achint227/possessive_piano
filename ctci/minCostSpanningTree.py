"""
given a graph with weighted undirected edges, find a tree that connects every node with minimum path cost

"""


class UnionFind:
    def __init__(self, items) -> None:
        self.components = {item: item for item in items}
        self.ranks = {item:1 for item in items}

    def find(self, a):
        while self.components[a] != a:
            a = self.components[a]
        return a

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        print(a, pa)
        print(b, pb)
        if pa == pb:
            return False
        if self.ranks[pa]<self.ranks[pb]:
            pa,pb=pb,pa
            a,b=b,a
        self.components[b] = pa
        self.ranks[pa]+=self.ranks[pb]
        self.ranks[pb]=0
        
        print(self.components)
        print(self.ranks)
        return True


edges = [
    ("A", "B", 2),
    ("A", "C", 3),
    ("A", "D", 1),
    ("B", "C", 4),
    ("B", "E", 3),
    ("C", "D", 2),
    ("C", "E", 5),
    ("D", "E", 4),
]


def minCostSpanningTree(graph):
    tree = []
    components = set()
    for s, d, _ in graph:
        components.add(s)
        components.add(d)

    uf = UnionFind(components)
    graph.sort(key=lambda x: x[2])
    for edge in graph:
        s, d, _ = edge
        if uf.union(s, d):
            tree.append(edge)
    return tree

    # Call the minCostSpanningTree function and print the result


result = minCostSpanningTree(edges)
print(result)
