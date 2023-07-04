# Derva Anargya Ghaly
# 24060121140149
# ASA C
# Source Code Algoritma Brute Force Shortest Path Semarang-Dieng

def brute_force_shortest_path(graph, start, goal):
    def generate_paths(current_node, visited, path, total_cost):
        if current_node == goal:
            return [(path + [current_node], total_cost)]
        paths = []
        neighbors = graph[current_node]
        
        for neighbor, cost in neighbors.items():
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [current_node]
                new_cost = total_cost + cost
                paths.extend(generate_paths(neighbor, visited, new_path, new_cost))
                visited.remove(neighbor)
        return paths
    
    visited = set([start])
    paths = generate_paths(start, visited, [], 0)
    
    if not paths:
        return None
    
    min_path, min_cost = min(paths, key=lambda x: x[1])
    return min_path, min_cost

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

result = brute_force_shortest_path(graph, start_node, goal_node)

if result:
    path, total_cost = result
    print("Rute Tercepat Menuju Dieng Plateu :", ' -> '.join(path))
    print("Total Jarak Yang Ditempuh :", total_cost)
else:
    print("Tidak ada rute yang tersedia dari", start_node, "ke", goal_node)
