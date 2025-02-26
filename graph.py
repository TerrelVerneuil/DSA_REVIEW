


# A Graph is a non-linear data structure consisting of vertices and edges
# verties are sometime refered to as nodes and the edges are lines or arcs
# that connect any two nodes in the graph


# unweighted implementation 
    
        
class Unweighted_Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        # n x n matrix
        self.graph = [[0 for i in range(nodes)] for j in range(nodes)]
    def add_edge(self, u, v):
        self.graph[u][v] = 1
    def print_graph(self):
        for i in range(len(self.graph)):
            print(self.graph[i])
    def remove_edge(self, u, v):
        self.graph[u][v] = 0
    def display_connected_nodes(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] == 1:
                    print(i, "->", j)

class Weighted_Graph:
    def __init__(self, nodes, weights):
        self.nodes = nodes
        self.weights = weights
        # n x n matrix
        self.graph = [[0 for i in range(nodes)] for j in range(nodes)]
    def add_edge(self, u, v, w):
        self.graph[u][v] = w
    def print_graph(self):
        for i in range(len(self.graph)):
            print(self.graph[i])
    def remove_edge(self, u, v):
        self.graph[u][v] = 0
    def shortest_path_from_start(self, start):
        for i in range(len(self.graph)):
            print(start, "->", i)
            




print("Unweighted Directed Graph")
ug = Unweighted_Graph(4)
ug.add_edge(0, 1)
ug.add_edge(0, 2)
ug.add_edge(1, 2)
ug.add_edge(2, 3)
ug.add_edge(3, 3)
print("Graph")
print(ug.print_graph())
print("Connected Nodes")
print(ug.display_connected_nodes())


