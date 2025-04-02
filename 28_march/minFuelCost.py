from collections import defaultdict
import math

def min_fuel_cost(roads_str, seats):
    roads = [list(map(int, pair.split())) for pair in roads_str.split(",")]
    
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    
    def dfs(node, parent):
        total_people = 1 
        total_fuel = 0
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            
            people_from_subtree, fuel_from_subtree = dfs(neighbor, node)
            total_people += people_from_subtree
            total_fuel += fuel_from_subtree + math.ceil(people_from_subtree / seats)
        
        return total_people, total_fuel
    
    
    _, fuel = dfs(0, -1)
    return fuel


roads_str = input("")
seats = int(input(""))
print(min_fuel_cost(roads_str, seats))