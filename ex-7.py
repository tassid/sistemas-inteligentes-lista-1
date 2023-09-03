from collections import deque
import time

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

# Medir o tempo de execução da Busca em Largura
tempo_inicio = time.time()
caminho_largura = busca_largura(mapa, inicio, destino)
tempo_fim = time.time()
tempo_busca_largura = tempo_fim - tempo_inicio

# Medir o tempo de execução da Busca em Profundidade
tempo_inicio = time.time()
caminho_profundidade = busca_profundidade(mapa, inicio, destino)
tempo_fim = time.time()
tempo_busca_profundidade = tempo_fim - tempo_inicio

# Medir o tempo de execução da Busca em Profundidade Iterativa
tempo_inicio = time.time()
caminho_profundidade_iterativa = busca_profundidade_iterativa(mapa, inicio, destino, limite=4)
tempo_fim = time.time()
tempo_busca_profundidade_iterativa = tempo_fim - tempo_inicio

# Imprimir resultados
print(f"Tempo de execução da Busca em Largura: {tempo_busca_largura} segundos")
print(f"Tempo de execução da Busca em Profundidade: {tempo_busca_profundidade} segundos")
print(f"Tempo de execução da Busca em Profundidade Iterativa: {tempo_busca_profundidade_iterativa} segundos")

# Determinar o algoritmo mais rápido
tempos = {
    "Busca em Largura": tempo_busca_largura,
    "Busca em Profundidade": tempo_busca_profundidade,
    "Busca em Profundidade Iterativa": tempo_busca_profundidade_iterativa
}

algoritmo_mais_rapido = min(tempos, key=tempos.get)
print(f"O algoritmo mais rápido foi: {algoritmo_mais_rapido}")
