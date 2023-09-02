from collections import deque

# Definindo a estrutura da árvore como um dicionário
# A chave é o nó e o valor é uma lista de seus filhos
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

# Busca em Largura (BFS)
def bfs(tree, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(child for child in tree[node] if child not in visited)

    return False

# Busca em Profundidade (DFS)
def dfs(tree, current, target, visited=None):
    if visited is None:
        visited = set()

    if current == target:
        return True

    visited.add(current)

    for neighbor in tree[current]:
        if neighbor not in visited:
            if dfs(tree, neighbor, target, visited):
                return True

    return False

# Encontrar nós 10 e 20 usando BFS
result_bfs = bfs(tree, 1, 10)
print("BFS - Nó 10 encontrado:", result_bfs)

result_bfs = bfs(tree, 1, 20)
print("BFS - Nó 20 encontrado:", result_bfs)

# Encontrar nós 10 e 20 usando DFS
result_dfs = dfs(tree, 1, 10)
print("DFS - Nó 10 encontrado:", result_dfs)

result_dfs = dfs(tree, 1, 20)
print("DFS - Nó 20 encontrado:", result_dfs)
