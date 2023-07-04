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
        print("Jalur saat ini :", ' -> '.join(path), "|| Cost saat ini :", total_cost)
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

print("Sebelum kita run, pilih algoritma dulu yuk!")
print("a. Brute Force")
print("b. Greedy")
choice = input("Masukkan pilihan (a atau b): ")

start_node = input("Masukkan start_node: ")
goal_node = input("Masukkan goal_node: ")

if choice == 'a':
    print("Menjalankan Brute Force...")
    result = brute_force_shortest_path(graph, start_node, goal_node)
    algorithm = "Brute Force"
elif choice == 'b':
    print("Menjalankan Greedy...")
    result = greedy_shortest_path(graph, start_node, goal_node)
    algorithm = "Greedy"
else:
    print("Pilihan tidak valid.")
    exit()

if result:
    path, total_cost = result
    print("Step by step:")
    for i, node in enumerate(path):
        current_path = ' -> '.join(path[:i+1])
        current_cost = sum(graph[path[j]][path[j+1]] for j in range(i))
        print("Jalur saat ini:", current_path, "|| Cost saat ini:", current_cost)
    print("\nRute Tercepat Menggunakan", algorithm, ":", ' -> '.join(path))
    print("Total Jarak Yang Ditempuh :", total_cost)
else:
    print("Tidak ada rute yang tersedia dari", start_node, "ke", goal_node)