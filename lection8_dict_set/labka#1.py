import ast
import doctest
import copy


def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name) as f:
        res = []
        for line in f:
            els = list(ast.literal_eval(line))
            line.split(",")
            res.append(els)
    return res


get_graph_from_file("data1.txt")


def to_edge_dict(edge_list):
    """
        (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    res = {}
    for i in edge_list:
        for x, j in enumerate(i):
            res[j] = sorted(res.get(j, []) + [i[1-x]])
    return res


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> dict

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3],\
 5: [1]}, (3, 1))
    False
    """
    return True if edge[1] in graph.get(edge[0], []) else False


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[1] not in graph.get(edge[0], []):
        graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
        graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]
    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[1] in graph.get(edge[0], []):
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph:
        graph[node] = []
    return graph


def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph:
        a = copy.copy(graph.get(node, []))
        for i in a:
            del_edge(graph, (node, i))
        del graph[node]
    return graph


def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    pass


doctest.testmod()
# COMMON NAMES -- INTERSECTION     &--intersection
