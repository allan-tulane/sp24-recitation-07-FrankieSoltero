from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current_node = frontier.pop()
        neighbors = graph[current_node]
        for n in neighbors:
            if n not in result:
                result.add(n)
                frontier.add(n)
        pass
    return result





def connected(graph):
    first_node = next(iter(graph))
    frontier = set([first_node])
    result = set([first_node])
    yesorno = False
    while len(frontier) != 0:
        current_node = frontier.pop()
        neighbors = graph[current_node]
        for n in neighbors:
            if n not in result:
                result.add(n)
                frontier.add(n)
    if len(result) == len(graph):
        yesorno = True
    return yesorno
    ### TODO
    pass




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    visited = set()
    components = 0
    for node in graph:
        if node not in visited:
            reachable_nodes = reachable(graph, node)
            visited.update(reachable_nodes)
            components += 1
    return components
    pass
