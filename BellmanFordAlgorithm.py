# Given the following graph structure
#
# graph = {
#     's' : {'t':6, 'y':7},
#     't' : {'x':5, 'z':-4, 'y':8 },
#     'y' : {'z':9, 'x':-3},
#     'z' : {'x':7, 's': 2},
#     'x' : {'t':-2}
# }
#
# implement the Bellman Ford algorithm to calculate the minimal distances from node s
#
# For example:
# Test: print(get_distances(graph, 's'))
# Result: {'s': 0, 't': 2, 'y': 7, 'z': -2, 'x': 4}


def get_distances(graph, start):
    result, predecessor = initialize(graph, start)
    for i in range(len(graph) - 1):
        for j in graph:
            for k in graph[j]:  # for all neighbors
                relax(j, k, graph, result, predecessor)

    for j in graph:  # checks for negative weights
        for k in graph[j]:
            assert result[k] <= result[j] + graph[j][k]

    return result


def initialize(graph, source):
    result = {}  # destination
    predecessor = {}  # previous node
    for node in graph:
        result[node] = float('Inf')
        predecessor[node] = None
    result[source] = 0  # source is always 0
    return result, predecessor


def relax(node, neighbour, graph, result, predecessor):
    if result[neighbour] > result[node] + graph[node][neighbour]:  # if the distance between node and neighbor is lower
        result[neighbour] = result[node] + graph[node][neighbour]
        predecessor[neighbour] = node


graph = {
    's' : {'t':6, 'y':7},
    't' : {'x':5, 'z':-4, 'y':8 },
    'y' : {'z':9, 'x':-3},
    'z' : {'x':7, 's': 2},
    'x' : {'t':-2}
}

# print(get_distances(graph, 's'))
# Result: {'s': 0, 't': 2, 'y': 7, 'z': -2, 'x': 4}
