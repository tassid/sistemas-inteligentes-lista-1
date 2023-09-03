def depth_limited_search(graph, start, goal, limit):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                elif len(path) < limit:
                    stack.append((neighbor, path + [neighbor]))
    return []

def iterative_deepening_search(graph, start, goal):
    depth = 0
    while True:
        result = depth_limited_search(graph, start, goal, depth)
        if result:
            return result
        depth += 1

def breadth_first_search(graph, start, goal):
    queue = [[start]]
    visited = set()
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            
            visited.add(node)
    
    return []

if __name__ == "__main__":
    # Mapa da Romênia como um dicionário de adjacência
    romania_map = {
        'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
        'Zerind': ['Arad', 'Oradea'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
        'Pitesti': ['Rimnicu Vilcea', 'Bucharest'],
        'Craiova': ['Rimnicu Vilcea', 'Drobeta'],
        'Bucharest': ['Fagaras', 'Pitesti'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova']
    }

    # Simulação da Busca em Profundidade
    print("Busca em Profundidade:")
    path_dfs = depth_limited_search(romania_map, 'Arad', 'Bucharest', float('inf'))  # Infinito para explorar tudo
    print(f"Caminho encontrado: {path_dfs}\n")

    # Simulação da Busca em Largura
    print("Busca em Largura:")
    path_bfs = breadth_first_search(romania_map, 'Arad', 'Bucharest')
    print(f"Caminho encontrado: {path_bfs}\n")

    # Simulação da Busca em Profundidade Iterativa
    print("Busca em Profundidade Iterativa:")
    path_iddfs = iterative_deepening_search(romania_map, 'Arad', 'Bucharest')
    print(f"Caminho encontrado: {path_iddfs}\n")
