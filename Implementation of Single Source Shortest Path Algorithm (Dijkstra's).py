import heapq

# ==========================================
# 1. DIJKSTRA'S ALGORITHM
# ==========================================

def dijkstra(graph, source):
    """
    graph: dict where graph[u] = [(v, weight), ...]
    source: starting vertex node label
    """
    # dist[v] <- INFINITY for all v; dist[source] <- 0
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    
    # prev[v] <- None for all v
    prev = {v: None for v in graph}
    
    # Priority Queue Q <- {(0, source)}
    Q = [(0, source)]
    
    # visited <- empty set
    visited = set()
    
    # WHILE Q is not empty:
    while Q:
        # d, u <- EXTRACT_MIN(Q)
        d, u = heapq.heappop(Q)
        
        # IF u IN visited: CONTINUE
        if u in visited:
            continue
            
        # ADD u to visited
        visited.add(u)
        
        # FOR each neighbor v of u with edge weight w:
        for v, w in graph[u]:
            # IF dist[u] + w < dist[v]:
            if dist[u] + w < dist[v]:
                # dist[v] <- dist[u] + w
                dist[v] = dist[u] + w
                
                # prev[v] <- u
                prev[v] = u
                
                # INSERT (dist[v], v) into Q
                heapq.heappush(Q, (dist[v], v))
                
    # RETURN dist[], prev[]
    return dist, prev


# ==========================================
# 2. PATH RECONSTRUCTION
# ==========================================

def reconstruct_path(prev, source, target):
    """
    Reconstructs the shortest path from source to target using the prev map.
    """
    path = []
    node = target
    
    # WHILE node IS NOT None:
    while node is not None:
        # PREPEND node to path
        path.insert(0, node)
        
        # node <- prev[node]
        node = prev.get(node)
        
    # IF path[0] = source: RETURN path
    if path and path[0] == source:
        return path
    # ELSE: RETURN [] // No path exists
    else:
        return []


# ==========================================
# EXAMPLE USAGE
# ==========================================
if __name__ == "__main__":
    # Define an adjacency list graph: u -> [(v, weight), ...]
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('B', 1), ('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }

    start_node = 'A'
    target_node = 'E'

    # Run Dijkstra
    distances, previous_nodes = dijkstra(graph, start_node)
    
    # Reconstruct path to target node
    shortest_path = reconstruct_path(previous_nodes, start_node, target_node)

    print(f"Shortest distances from '{start_node}': {distances}")
    print(f"Shortest path from '{start_node}' to '{target_node}': {shortest_path}")
    print(f"Total distance: {distances[target_node]}")