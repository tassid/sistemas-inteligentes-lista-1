from collections import deque
import time

# Árvore no formato de dicionário
tree = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [9, 10],
    5: [11],
    6: [],
    7: [12, 13],
    8: [14],
    9: [],
    10: [15, 16, 17],
    11: [18, 19, 20],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [21, 22],
    18: [],
    19: [],
    20: [],
    21: [],
    22: []
}

def bfs(tree, start, targets):
    visited = set()
    queue = deque([(start, [])])
    nodes_visited = 0
    nodes_expanded = 0

    while queue:
        node, path = queue.popleft()
        visited.add(node)
        nodes_visited += 1

        if node in targets:
            print(f"Nós visitados durante a BFS: {nodes_visited}")
            print(f"Nós expandidos durante a BFS: {nodes_expanded}")
            print(f"Caminho encontrado para o nó {node}: {path + [node]}")
            targets.remove(node)

        for neighbor in tree.get(node, []):
            if neighbor not in visited and neighbor not in [n[0] for n in queue]:
                queue.append((neighbor, path + [node]))
                nodes_expanded += 1

        # Medir o uso de memória após cada iteração
        memory_usage = get_memory_usage()
        print(f"Uso de memória durante a BFS: {memory_usage:.2f} MB")

def dfs(tree, node, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    nodes_visited = 1

    if node == target:
        print(f"Nós visitados durante a DFS: {nodes_visited}")
        print(f"Caminho encontrado para o nó {node}: {path + [node]}")
        return True

    for neighbor in tree.get(node, []):
        if neighbor not in visited:
            nodes_visited += 1
            if dfs(tree, neighbor, target, visited, path + [node]):
                print(f"Nós visitados durante a DFS: {nodes_visited}")
                return True

        # Medir o uso de memória após cada iteração
        memory_usage = get_memory_usage()
        print(f"Uso de memória durante a DFS: {memory_usage:.2f} MB")

def get_memory_usage():
    import psutil
    process = psutil.Process()
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Em megabytes
    return memory_usage

# Medir o tempo de execução e uso de memória em cada execução BFS e DFS
start_time = time.time()

# Encontrar o nó 10 usando BFS
print("Busca em Largura (BFS) para encontrar o nó 10:")
bfs(tree, 1, [10])

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução da BFS para encontrar o nó 10: {execution_time} segundos")

print("\n------------------------------------------\n")

start_time = time.time()

# Encontrar o nó 20 usando BFS
print("Busca em Largura (BFS) para encontrar o nó 20:")
bfs(tree, 1, [20])

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução da BFS para encontrar o nó 20: {execution_time} segundos")

print("\n------------------------------------------\n")

start_time = time.time()

# Encontrar o nó 10 usando DFS
print("Busca em Profundidade (DFS) para encontrar o nó 10:")
dfs(tree, 1, 10)

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução da DFS para encontrar o nó 10: {execution_time} segundos")

print("\n------------------------------------------\n")

start_time = time.time()

# Encontrar o nó 20 usando DFS
print("Busca em Profundidade (DFS) para encontrar o nó 20:")
dfs(tree, 1, 20)

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução da DFS para encontrar o nó 20: {execution_time} segundos")
