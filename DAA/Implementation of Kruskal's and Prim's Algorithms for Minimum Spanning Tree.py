import heapq

# ==========================================
# 1. KRUSKAL'S ALGORITHM (Disjoint Set / Union-Find)
# ==========================================

class DisjointSet:
    def __init__(self, vertices):
        # Parent of each node points to itself initially
        self.parent = {v: v for v in vertices}
        # Rank used to keep tree balanced during union
        self.rank = {v: 0 for v in vertices}

    def find(self, i):
        """Finds the root of the set containing 'i' with path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, u, v):
        """Unites two sets by rank."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(vertices, edges):
    """
    vertices: list of vertex labels, e.g., ['A', 'B', 'C', ...]
    edges: list of tuples (u, v, w) representing an edge between u and v with weight w
    """
    # 1. Sort all edges by weight in non-decreasing order
    sorted_edges = sorted(edges, key=lambda item: item[2])
    
    # 2. Create Union-Find structure
    ds = DisjointSet(vertices)
    
    # 3. MST initialization
    mst = []
    
    # 4. Process edges
    for u, v, w in sorted_edges:
        if ds.find(u) != ds.find(v):  # No cycle
            mst.append((u, v, w))
            ds.union(u, v)
            if len(mst) == len(vertices) - 1:
                break
                
    return mst


# ==========================================
# 2. PRIM'S ALGORITHM (Priority Queue / Min-Heap)
# ==========================================

def prim(vertices, adj_list, start):
    """
    vertices: list of vertex labels
    adj_list: dict where adj_list[u] = [(v, weight), ...]
    start: starting vertex
    """
    key = {v: float('inf') for v in vertices}
    parent = {v: None for v in vertices}
    in_mst = {v: False for v in vertices}
    
    key[start] = 0
    
    # Priority Queue holds tuples of (key_weight, vertex)
    Q = [(0, start)]
    
    while Q:
        weight, u = heapq.heappop(Q)
        
        # Skip stale priority queue entries
        if in_mst[u]:
            continue
            
        in_mst[u] = True
        
        for v, w in adj_list[u]:
            if not in_mst[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(Q, (w, v))
                
    return parent


# ==========================================
# EXAMPLE USAGE
# ==========================================
if __name__ == "__main__":
    nodes = ['A', 'B', 'C', 'D', 'E']
    
    # Edge list format for Kruskal: (u, v, weight)
    edge_list = [
        ('A', 'B', 2),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 1),
        ('B', 'E', 4),
        ('C', 'E', 5),
        ('D', 'E', 1)
    ]
    
    # Adjacency list format for Prim: u -> [(v, weight), ...]
    adjacency_list = {v: [] for v in nodes}
    for u, v, w in edge_list:
        adjacency_list[u].append((v, w))
        adjacency_list[v].append((u, w))  # Undirected graph

    # Run Kruskal
    kruskal_mst = kruskal(nodes, edge_list)
    print("Kruskal's MST Edges:", kruskal_mst)

    # Run Prim
    prim_parents = prim(nodes, adjacency_list, start='A')
    prim_mst = [(parent, node, adjacency_list[parent]) for node, parent in prim_parents.items() if parent is not None]
    
    print("\nPrim's MST Parent Tree:")
    for node, p in prim_parents.items():
        if p is not None:
            print(f"Edge: ({p} - {node})")