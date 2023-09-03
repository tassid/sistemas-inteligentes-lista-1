from collections import deque

def busca_largura(mapa, inicio, destino):
    fila = deque()
    fila.append([inicio])
    while fila:
        caminho = fila.popleft()
        no_atual = caminho[-1]
        if no_atual == destino:
            return caminho
        for vizinho in mapa.get(no_atual, []):
            if vizinho not in caminho:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
    return None

def busca_profundidade(mapa, inicio, destino):
    pilha = []
    pilha.append([inicio])
    while pilha:
        caminho = pilha.pop()
        no_atual = caminho[-1]
        if no_atual == destino:
            return caminho
        for vizinho in mapa.get(no_atual, []):
            if vizinho not in caminho:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                pilha.append(novo_caminho)
    return None

def busca_profundidade_iterativa(mapa, inicio, destino, limite):
    for profundidade_limite in range(1, limite + 1):
        resultado = busca_profundidade_limitada(mapa, inicio, destino, profundidade_limite)
        if resultado:
            return resultado
    return None

def busca_profundidade_limitada(mapa, no_atual, destino, limite):
    if limite == 0 and no_atual != destino:
        return None
    if no_atual == destino:
        return [no_atual]
    for vizinho in mapa.get(no_atual, []):
        caminho = busca_profundidade_limitada(mapa, vizinho, destino, limite - 1)
        if caminho:
            return [no_atual] + caminho
    return None

# Exemplo de mapa com conexão indireta
mapa = {
    'Home': {'Museum': 2.7, 'Club': 1.2, 'Bank': 1.3},
    'Museum': {'Park': 1.6, 'Bank': 1.7},
    'Park': {'Lake': 1.6, 'Bank': 1.8},
    'Lake': {'School': 0.9},
    'School': {'Club': 1.4, 'Bank': 1},
    'Bank': {'Club': 1.1, 'Lake': 1, 'Museum': 0.5}
}

inicio = 'School'
destino = 'Museum'

# Busca em Largura
caminho_largura = busca_largura(mapa, inicio, destino)

# Busca em Profundidade
caminho_profundidade = busca_profundidade(mapa, inicio, destino)

# Busca em Profundidade Iterativa (com limite de 4)
caminho_profundidade_iterativa = busca_profundidade_iterativa(mapa, inicio, destino, limite=4)

# Avaliar qual algoritmo encontrou o caminho mais curto
distancia_largura = sum(mapa[caminho_largura[i]][caminho_largura[i+1]] for i in range(len(caminho_largura)-1)) if caminho_largura else float('inf')
distancia_profundidade = sum(mapa[caminho_profundidade[i]][caminho_profundidade[i+1]] for i in range(len(caminho_profundidade)-1)) if caminho_profundidade else float('inf')
distancia_profundidade_iterativa = sum(mapa[caminho_profundidade_iterativa[i]][caminho_profundidade_iterativa[i+1]] for i in range(len(caminho_profundidade_iterativa)-1)) if caminho_profundidade_iterativa else float('inf')

# Imprimir resultados
print(f"Caminho encontrado pela Busca em Largura: {caminho_largura}, Distância: {distancia_largura} km")
print(f"Caminho encontrado pela Busca em Profundidade: {caminho_profundidade}, Distância: {distancia_profundidade} km")
print(f"Caminho encontrado pela Busca em Profundidade Iterativa: {caminho_profundidade_iterativa}, Distância: {distancia_profundidade_iterativa} km")

# Determinar o melhor algoritmo
melhor_algoritmo = None
menor_distancia = float('inf')

if caminho_largura and distancia_largura < menor_distancia:
    melhor_algoritmo = "Busca em Largura"
    menor_distancia = distancia_largura

if caminho_profundidade and distancia_profundidade < menor_distancia:
    melhor_algoritmo = "Busca em Profundidade"
    menor_distancia = distancia_profundidade

if caminho_profundidade_iterativa and distancia_profundidade_iterativa < menor_distancia:
    melhor_algoritmo = "Busca em Profundidade Iterativa"
    menor_distancia = distancia_profundidade_iterativa

print(f"Melhor algoritmo: {melhor_algoritmo}")
