# Implement in Python 3 the Minimum Spanning Tree named create_spanning_tree using the Prim's Algorithm.
# (1) Use the following representation for a graph.
#     example_graph = {
#         'A': {'B': 2, 'C': 3},
#         'B': {'A': 2, 'C': 12, 'D': 10, 'E': 4},
#         'C': {'A': 3, 'B': 12, 'F': 5},
#         'D': {'B': 10, 'E': 7},
#         'E': {'B': 4, 'D': 7, 'F': 16},
#         'F': {'C': 5, 'E': 16, 'G': 9},
#         'G': {'F': 9},
#     }
#
# (2) dict(create_spanning_tree(example_graph, 'D'))) must return the following spaning tree:
#     {'D': {'E'}, 'E': {'B'}, 'B': {'A'}, 'A': {'C'}, 'C': {'F'}, 'F': {'G'}}
#
# (3) you may import the following to simplify the implementation:
#     from collections import defaultdict
#     import heapq
#
# For example:
#
# Test
#     example_graph = {
#         'A': {'B': 2, 'C': 3},
#         'B': {'A': 2, 'C': 12, 'D': 10, 'E': 4},
#         'C': {'A': 3, 'B': 12, 'F': 5},
#         'D': {'B': 10, 'E': 7},
#         'E': {'B': 4, 'D': 7, 'F': 16},
#         'F': {'C': 5, 'E': 16, 'G': 9},
#         'G': {'F': 9},
#     }
#     print(dict(create_spanning_tree(example_graph, 'D')))
#
# Result: {'D': {'E'}, 'E': {'B'}, 'B': {'A'}, 'A': {'C'}, 'C': {'F'}, 'F': {'G'}}

from collections import defaultdict
import heapq


def create_spanning_tree(graph, start):
    mst = defaultdict(set)
    visited = set([start])
    edges = [(cost, start, nextEdge) for nextEdge, cost in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        cost, currentEdge, nextEdge = heapq.heappop(edges)
        if nextEdge not in visited:
            visited.add(nextEdge)
            mst[currentEdge].add(nextEdge)
            for afterNextEdge, cost in graph[nextEdge].items():
                if afterNextEdge not in visited:
                    heapq.heappush(edges, (cost, nextEdge, afterNextEdge))
    return mst


example_graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 12, 'D': 10, 'E': 4},
        'C': {'A': 3, 'B': 12, 'F': 5},
        'D': {'B': 10, 'E': 7},
        'E': {'B': 4, 'D': 7, 'F': 16},
        'F': {'C': 5, 'E': 16, 'G': 9},
        'G': {'F': 9},
    }

print(dict(create_spanning_tree(example_graph, 'D')))