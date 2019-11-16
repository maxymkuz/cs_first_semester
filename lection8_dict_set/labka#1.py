import ast
import doctest

def get_graph_from_file(file_name):
    """ 
    (str) -> (list)
    
    Read graph from file and return a list of edges.
    
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name) as f:
        # lines = f.readlines()
        # print(lines)
        res = []
        for line in f:
            els = list(ast.literal_eval(line))
            line.split(",")
            # print(els)
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
        for x, j  in enumerate(i):
            res[j] = sorted(res.get(j, []) + [i[1-x]])
    return res


doctest.testmod()


def is_edge_in_graph(graph, edge):
    """ 
    (dict, tuple) -> dict
    
    Return True if graph contains a given edge and False otherwise.
    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    return True if edge[1] in graph.get(edge[0], []) else False


is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))




# COMMON NAMES -- INTERSECTION     &--intersection