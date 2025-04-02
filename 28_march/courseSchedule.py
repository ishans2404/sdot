from collections import deque

def can_finish_courses():
    
    N = int(input())  
    M = int(input())  
    
   
    graph = {i: [] for i in range(N)}
    in_degree = [0] * N
    
    for _ in range(M):
        ai, bi = map(int, input().split())
        graph[bi].append(ai)
        in_degree[ai] += 1
    
  
    queue = deque([i for i in range(N) if in_degree[i] == 0])
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    print(1 if count == N else 0)

can_finish_courses()