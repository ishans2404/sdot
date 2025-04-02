import heapq

def prims_mst(V, G):
    key = [float('inf')] * V   
    parent = [-1] * V         
    min_heap = [(0, 0)]        
    key[0] = 0                 
    visited = set()            
    mst_cost = 0

    while len(visited) < V:
        weight, u = heapq.heappop(min_heap)  
        
        if u in visited:
            continue
        
        visited.add(u)
        mst_cost += weight  
        
        for v in range(V):
            if v not in visited and G[u][v] > 0 and G[u][v] < key[v]:  
                key[v] = G[u][v]  
                heapq.heappush(min_heap, (G[u][v], v))
                parent[v] = u  

    return mst_cost

def main():
    V = int(input().strip())  
    G = [list(map(int, input().split())) for _ in range(V)]  

    print(prims_mst(V, G))

if _name_ == "_main_":
    main()