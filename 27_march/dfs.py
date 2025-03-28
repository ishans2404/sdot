class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self):
        visited = [False] * self.vertices
        for v in range(self.vertices):
            if not visited[v]:
                self.dfs_util(v, visited)


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(2, 3)

print("DFS Traversal of the graph:")
g.dfs()