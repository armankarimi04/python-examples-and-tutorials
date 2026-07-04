# A graph is an abstract data type
# in which a piece of data connects to one or more other pieces of data

# each piece of data in a graph is caled a vertex or a node

# a vertex has a name called key

# a vertex can have additional data called payload

# the connection between vertices in a graph is called an edge

# a graph's edge can contain a weight which is the cost to travel between vertices

# example; a graph could represent a map, each vertex can be a city, the weight between two vertices could be the distance between them

# there are several types of graphs: directed graphs, undirected graphs, and complete graphs. 
# directed: each edge has a direction associated with it and you can only move between two vertices only in that direction

# direction can be two-way.
# a directed graph is an excellent choice for creating a graph representing a social network with followers
# e.g. you can use a vector (directed line) to show that you're following another user, but he/she is not following you

# undirected graph is one in which the edges are bidrectional (a line without arrows). you can travel in either direction. between the two.
# like being friends in facebook.

# a complete graph: every vertex is connected to every other one

# incomplete graph: some but not all vertices are connected

# a graph path: a sequence of vertices connected by edges

# a cycle: a path in a graph starting and ending at the same vertex

# an acyclic graph: a graph that does not contain a cycle

# a tree is a restricted form of graph. they have direction (parent to child), do not contain cycles
# they are directed acyclic graphs with a restriction: a child can have only one parent

# There are several ways to create graphs programmatically. For example, you can use an edge list, an adjacency matrix, or an adjacency list.

# An edge list is a data structure where you represent each edge in a graph with two vertices that connect
a_graph_from_list = [
    [10, 20],
    [10, 30],
    [20, 10],
    [20, 30],
    [30, 10],
    [30, 20],
    [30, 40],
    [40, 30]
]


# another way to represent a graph is by using an adjacency matrix
# an adjacency matrix is a two-dimensional array of rows and columns that contains a graph's vertices
# the intersection of each row and column is used to represent an edge
# tradiotionally, 1 for vertices that connect and 0 for vertices that do not
# when two vertices are connected they are adjacent

# one problem with this approach is sparsity or empty cells, so adjacency matrices are not very efficient (because of large number of empty cells)
# (inefficient use of computer memory)

# another approach is an adjacency list
# a collection of unordered lists, with each list representing the connection for a single vertex
a_graph_from_adjacency_list = {
    10: [20, 30],
    20: [10, 30],
    30: [10, 20, 40],
    40: [30]
}

# there are different ways to implement graphs

# adding a vertex and an edge to a graph is O(1)

# searching, deleting, and other algorithms depend on the implementation and the ds used: arrays, linked lists, hash tables

# generally the performance of basic operations depend on either number of vertices or edges or combination of the two

# graphs are highly used in social medias such as twitter and instagram

# also sometimes used in networks

# another extremely useful case is for maps (city maps, roads, routes)
# finding the fastest path between destinations

# helpful for computer graphics (points, lines, 2d and 3d shapes)

# Search engines use graphs often to determine search ranking based on the connectiviy of search and results

# OS and programming languages use graphs in memory manangement

# An adjacency list in python
from typing import Union

class Vertex:   
    def __init__(self, key):
        self.key = key # represents the vertex's key (value)
        self.connections = {} # any vertex adjacent to this vertex
        
    def add_adj(self, vertex, weight=0):
        # Adds another vertex as an adjacent to this one
        self.connections[vertex] = weight
        
    def get_connections(self):
        return self.connections.keys()

    def get_weight(self, vertex):
        return self.connections[vertex]

    
class Graph:
    def __init__(self):
        # self.vertex_dict = dict[Vertex, Union[int, str]] = {} # wrong
        self.vertex_dict = dict[Union[int, str], Vertex] = {} # right
        # vertex_dict stores the vertices stored in each graph
        
    def add_vertex(self, key) -> None:
        if key in self.vertex_dict: # this check is my own
            raise Exception("A vertex with this key already exists in the graph.")
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex
        
    def get_vertex(self, key) -> Vertex | None:
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        return None
    
    def add_edge(self, f, t, weight=0):
        if f not in self.vertex_dict:
            self.add_vertex(f)
        if t not in self.vertex_dict:
            self.add_vertex(t)
        self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)
        
        
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 10)
    vertex_a = graph.get_vertex("A")
    vertex_b = graph.get_vertex("B")
    
    
# Dijkstra's Algorithm

# when working with graphs, one often needs to find the shortest path between two vertices.
# one very famous in this area is the Dijkstra's Algorithm (invented by Edsger Dijkstra)

# it can be used to find the shortest path from a vertex to every other vertex

# we need to use a priority queue for this (a heap is an impelmentaiton of priority queues)
# a binary heap is a type of heap

# we start from A
# we keep track of all paths in a dict
# visiting a vertex means popping it off the queue

import heapq

def dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph} # equals the infinity in math
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)] # priority queue
    
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_distance]:
            continue
        
        for neighbor, weight in graph[current_distance].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

