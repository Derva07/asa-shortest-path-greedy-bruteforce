# Derva Anargya Ghaly
# 24060121140149
# ASA C
# Source Code Algoritma Greedy Shortest Path Semarang-Dieng

def greedy_shortest_path(graph, start, goal):
    current_node = start
    path = [current_node]
    total_cost = 0
    
    while current_node != goal:
        neighbors = graph[current_node]
        next_node = None
        min_cost = float('inf')
        
        for neighbor, cost in neighbors.items():
            if neighbor not in path and cost < min_cost:
                next_node = neighbor
                min_cost = cost
                
        if next_node is None:
            return None
        
        path.append(next_node)
        total_cost += min_cost
        current_node = next_node
    return path, total_cost

graph = {
    'Semarang': {'Mijen': 20, 'Bandungan': 33},
    'Mijen': {'Semarang': 20, 'Boja': 10},
    'Bandungan': {'Semarang': 33, 'Boja': 25, 'Kaloran': 23},
    'Boja': {'Mijen': 10, 'Bandungan': 25, 'Muntung': 43},
    'Muntung': {'Boja': 43, 'Kaloran': 28, 'Dieng' : 25},
    'Kaloran': {'Bandungan': 23, 'Muntung': 28, 'Dieng': 57},
    'Dieng': {'Muntung': 25, 'Kaloran': 57}
}

start_node = 'Semarang'
goal_node = 'Dieng'

result = greedy_shortest_path(graph, start_node, goal_node)

if result:
    path, total_cost = result
    print("Rute Tercepat Adalah :", ' -> '.join(path))
    print("Total Jarak Yang Ditempuh :", total_cost)
else:
    print("Tidak ada rute yang tersedia dari", start_node, "ke", goal_node)