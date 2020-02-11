#Uses python3
import sys
import math

# The “clusters” are the connected components that Kruskal’s 
# algorithm has created after a certain point.

class Node:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.parent = p
        self.rank = 0

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.weight = w

def euclidean_distance(x1, y1, x2, y2):
  return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def Find(i, nodes):
  if (i != nodes[i].parent) :
        nodes[i].parent = Find(nodes[i].parent, nodes)
  return nodes[i].parent

def Union(u, v, nodes):
    r1 = Find(u, nodes)
    r2 = Find(v, nodes)
    if (r1 != r2):
        if (nodes[r1].rank > nodes[r2].rank):
            nodes[r2].parent = r1
        else:
            nodes[r1].parent = r2
            if (nodes[r1].rank == nodes[r2].rank):
                nodes[r2].rank += 1

def clustering(x, y, k):
    #initialization
    n = len(x)
    edges = []
    nodes = []
    
    #initialize nodes with xy-coordinates and index
    for i in range(n):
       nodes.append(Node(x[i], y[i], i))
    
    #initialize edges with the Euclidean distance between coordinates
    for i in range(n):
        for j in range(i+1, n):
            edges.append(Edge(i, j, euclidean_distance(x[i], y[i], x[j], y[j])))
    
    edges = sorted(edges, key=lambda edge: edge.weight)
    
	#maintain clusters as a set of connected components of a graph.
	#iteratively combine the clusters containing the two closest items by adding an edge between them.
    num_edges_added = 0
    for edge in edges:
        if Find(edge.u, nodes) != Find(edge.v, nodes):
            num_edges_added += 1
            Union(edge.u, edge.v, nodes)
		#stop when there are k clusters
        if(num_edges_added > n - k): 
            return edge.weight
    return -1.0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
