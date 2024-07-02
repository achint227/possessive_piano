"""
Given two nodes in a graph, find the length of the shortest distance between them
"""

from collections import deque


def get_neighbors(graph, node):
    return graph[node]


def shortest_path_length(graph, n1, n2):
    # start 2 bfs from each node
    # if the paths intersect, then we founf the shortest path

    path1 = set()
    path2 = set()
    path_length = 0
    q1 = deque([n1])
    path1.add(n1)
    q2 = deque([n2])
    path2.add(n2)
    while q1 and q2:
        if q1:
            path_length += 1
            s1 = q1.popleft()
            if s1 in path2:
                return path_length
            for n1 in get_neighbors(graph, s1):
                if n1 not in path1:
                    q1.append(n1)
                    path1.add(n1)
        if q2:
            path_length += 1
            s2 = q2.popleft()
            if s2 in path1:
                return path_length
            for n2 in get_neighbors(graph, s2):
                if n2 not in path2:
                    q2.append(n2)
                    path2.add(n2)
    return path_length


def main():
    # Define your graph
    graph = {
        "A": ["B", "C", "D"],
        "B": ["A", "D", "E"],
        "C": ["A", "E", "F"],
        "D": ["A", "B", "E", "G"],
        "E": ["B", "C", "D", "F", "G"],
        "F": ["C", "E", "H"],
        "G": ["D", "E", "H"],
        "H": ["F", "G"],
    }

    # Define the nodes you want to find the shortest path between
    node1 = "A"
    node2 = "H"

    # Call the shortest_path_length function to get the shortest path length
    shortest_length = shortest_path_length(graph, node1, node2)

    # Print the result
    print(f"The shortest path length between {node1} and {node2} is {shortest_length}")


if __name__ == "__main__":
    main()
