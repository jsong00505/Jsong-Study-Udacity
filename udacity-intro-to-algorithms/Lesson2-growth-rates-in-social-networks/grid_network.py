import math


# this is how I calculate the m of n
# I supposed n should be a perfect squared number of one number
def calculate_edges(n):
    nSqrt = math.sqrt(n)
    m = nSqrt * (nSqrt - 1) * 2
    return m

print calculate_edges(256)

# this is how the teacher solve this problem
# Just use "ring_network" algorithm

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

# Make an empty graph
G = {}

n = 256
side = int(math.sqrt(n))
# Add in the edges
for i in range(side):
    for j in range(side):
        if i < side - 1: make_link(G, (i,j), (i + 1, j))
        if j < side - 1: make_link(G, (i, j), (i, j + 1))

# How many nodes?
print len(G)

# How many edges?
print sum([len(G[node]) for node in G.keys()]) /2

print G

