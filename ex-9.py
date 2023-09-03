def depth_limited_search(graph, node, goal, limit):
    if node == goal:
        return [node]
    elif limit == 0:
        return []
    else:
        for neighbor in graph[node]:
            path = depth_limited_search(graph, neighbor, goal, limit - 1)
            if path:
                return [node] + path
        return []

def iterative_deepening_search(graph, start, goal):
    depth = 0
    while True:
        result = depth_limited_search(graph, start, goal, depth)
        if result:
            return result
        depth += 1

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

    # Teste com limites 2, 4 e 7
    limites = [2, 4, 7]

    for limite in limites:
        print(f"Busca em Profundidade Limitada com limite {limite}:")
        path = depth_limited_search(romania_map, 'Arad', 'Bucharest', limite)
        if path:
            print(f"Caminho encontrado: {path}")
        else:
            print("Nenhum caminho encontrado.")
        print()

    # Teste com aprofundamento iterativo
    print("Aprofundamento Iterativo:")
    path = iterative_deepening_search(romania_map, 'Arad', 'Bucharest')
    if path:
        print(f"Caminho encontrado: {path}")
    else:
        print("Nenhum caminho encontrado.")
