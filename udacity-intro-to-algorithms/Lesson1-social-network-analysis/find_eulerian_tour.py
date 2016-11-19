# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

""" comment out for a while
This was my first try, but it was failed...
def find_eulerian_tour(graph):
    # your code here
    degree = get_degree(graph)
    nodes = degree.keys()
    if check_odd(nodes, degree):
        connected = connected_nodes(graph)
    else:
        return False
    print "connected --> ", connected
    result = []
    if connected.__len__() == nodes.__len__():
        for e in connected:
            result.append(e)
    result.append(result[0])
    return result
"""
def find_eulerian_tour(graph):
    # your code here
    degree = get_degree(graph)
    nodes = degree.keys()

    maxDegree = 0
    biggest = 0

    for key, value in degree.iteritems():
        if biggest < value:
            maxDegree = key
            biggest = value

    result = []
    if check_odd(nodes, degree):
        # init
        x = graph[maxDegree][0]
        y = graph[maxDegree][1]
        result.append(x)
        result.append(y)
        graph.remove((x, y))
        for i in range(graph.__len__()):
            for edge in graph:
                if y == edge[0] and x != edge[1]:
                    result.append(edge[1])
                    x = edge[0]
                    y = edge[1]
                    graph.remove((x, y))
                    break
                elif y == edge[1] and x != edge[0]:
                    result.append(edge[0])
                    x = edge[1]
                    y = edge[0]
                    graph.remove((y, x))
                    break
    return result



# These functions are required to find Eulerian Tour.
def check_odd(nodes, degree):
    for node in nodes:
        try:
            e = degree[node]
            if e % 2 == 1:
                return False
        except:
            return False
    return True

def get_x_y_list(graph):
    dict = {}
    for edge in graph:
        dict[edge[0]] = edge[1]
    return dict
def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes



print find_eulerian_tour([(1, 2), (2, 3), (3, 1)])  # passed
print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]) # passed

print find_eulerian_tour([(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)])
