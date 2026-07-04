# in this file we'll implement Dijkstra's Algorithm

# we'll be using a heap and graph

# Heap is an implementation of a priority queue. we'll use it for a breadth-first search
# in breadth-first search, we start at the root of the tree, and check every child node

# 1. first we'll start by creating a dictionary that will keep track of all shortest paths
# at first, this dict has only A which is set to 0. (travel time from A to A is 0). And to all other nodes we set to infinity (because paths weights are unknown right now, we infinity to represent that)
# at this point we haven't visited any vertices. Visiting vertices means popping it off the priority queue
# if we haven't found a shorter path from the starting index to it, we look at all the vertices adjacent to it for a shorter path to the starting vertex
# if we a shorter path, we put the adjacent vertex to on the priority queue

# at this point, we'll only have one vertex in pq (A, 0), we pop it and check to see if there is a shorter path to this vertex.
# if the current path is already the shortest, we don't need to do anything, we continue to iterate, in this case we iterate all vertices adjacent to vertex A

# then we move on to B and C
# we put them both in the priority queue along with their weight

# vertices checked: A,
# vertices unchecked: B, C, D
# priority queue = [(2, B), (6, C)]
# distances = {
    # A: 0,
    # B: 2,
    # C: 6
    # D: still inf  
# }

# now we pop B, why? because it has the highest priority (2)
# we have not found a shorter path from B to the starting vertex yet
# so we continue
# we check for all adjacent vertices for a shorter path
# B only has one adjacent vertex with a shorter path (D), so we add D to dict (along with its weight)

# vertices checked: A, B
# vertices unchecked: D, C
# priority queue = [(6, C), (7, D)]
# distances = {
    # A: 0,
    # B: 2,
    # C: 6
    # D: 7
# }

# now we pop C from priority queue because it has the shortest path in the queue
# C is also adjacent to D, but its distance from starting vertex is 14 and we've already found a shorter path to D. so we don't add D again
# ignoring longer paths is what makes this algorithm efficent

# vertices checked: A, B, C
# vertices unchecked: D
# priority queue = [(7, D)]
# distances = { unchanged
    # A: 0,
    # B: 2,
    # C: 6
    # D: 7
# }

# vertex D is not adjacent to any other vertices, so we pop it off
# now the priority queue is empty, algorithm is complete.

# vertices checked: A, B, C, D
# vertices unchecked:
# priority queue = []
# distances = { unchanged
    # A: 0,
    # B: 2,
    # C: 6
    # D: 7
# }

import heapq

# IMPORTANT
# this implementation uses a dict of dicts as a graph not the Graph class from eariler

def dijkstra(graph, starting_vertex) -> dict:
    
    # a dict holding paths from the starting vertex to each other vertex
    # {'A': inf, 'B': inf, 'C': inf, 'D': inf} (at the beginning)
    distances = {vertex: float('infinity') for vertex in graph}
    
    # we update the initial item (the starting_vertex self with weight of 0)
    # {'A': 0, 'B': inf, 'C': inf, 'D': inf}
    distances[starting_vertex] = 0
    
    priority_queue = [(0, starting_vertex)]
    while len(priority_queue) > 0: # as long as there is one or more items in priority queue
        
        # priority_queue will automatically gives us the vertex with shortest distance
        # because it is a min heap
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # we are only interested if the path is shorter than the shortest path in our queue
        if current_distance > distances[current_vertex]:
            continue # jumps back to the top
        
        # otherwise, we check all adjacent vertices of the current vertex
        for neigbor, weight in graph[current_vertex].items():
            
            # for each vertex, we calcualte its distance from starting_vertex
            # by adding its weight to current_distance
            distance = current_distance + weight
            
            # if the path for that adjacent vertex is shorter that the path already inside
            if distance < distances[neigbor]:
                
                # we update the dict and push it into priority_queue
                distances[neigbor] = distance
                heapq.heappush(priority_queue, (distance, neigbor))
    return distances
    
    
def main() -> None:
    graph = { # a graph in shape of adjacency list
        'A': {'B': 2, 'C': 6},
        'B': {'D': 5},
        'C': {'D': 8},
        'D': {},
    }
    
    dijkstra(graph=graph, starting_vertex='A')
    
    print(dijkstra(graph, 'A'))
    
    
if __name__ == "__main__":
    main()
    
# Challenge:
# Modify Dijkstra’s algorithm so it only returns the path from a starting vertex to another vertex you pass in