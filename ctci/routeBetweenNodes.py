"""
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""

from collections import deque


def get_neighbors(node, graph):
    return graph[node]


def are_connected(graph, node1, node2):

    visited = set([node1])

    q = deque([node1])

    while q:
        for _ in range(len(q)):
            curr = q.pop()
            if curr == node2:
                return True
            for node in get_neighbors(curr, graph):
                q.append(node)
                visited.add(node)
    return False


def main():
    # Define the directed graph
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": [],
        "E": ["F"],
        "F": [],
        "G": ["B"],
    }

    # Define the nodes to check for connectivity
    node1 = "A"
    node2 = "G"

    # Check if the nodes are connected
    connected = are_connected(graph, node1, node2)

    # Print the result
    if connected:
        print(f"There is a route between {node1} and {node2}.")
    else:
        print(f"There is no route between {node1} and {node2}.")


if __name__ == "__main__":
    main()
