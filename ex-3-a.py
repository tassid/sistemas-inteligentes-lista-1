from collections import deque

# Função para criar um mapa simples
def criar_mapa():
    return {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
        'F': [],
    }

# Função para verificar se a solução é válida
def is_solution(mapa):
    for regiao, cores in mapa.items():
        for vizinha in mapa[regiao]:
            if cores == mapa[vizinha]:
                return False
    return True

# Função para gerar os sucessores do estado atual
def generate_successors(mapa):
    estados_sucessores = []
    regioes = list(mapa.keys())

    # Encontra a próxima região a ser colorida (ainda não colorida)
    for regiao in regioes:
        if not mapa[regiao]:
            regiao_a_colorir = regiao
            break

    if not mapa[regiao_a_colorir]:
        for cor in range(1, 5):  # Supomos que temos 4 cores disponíveis
            novo_mapa = mapa.copy()
            novo_mapa[regiao_a_colorir] = cor

            # Verifica se o novo estado é válido
            if is_solution(novo_mapa):
                estados_sucessores.append(novo_mapa)

    return estados_sucessores

# Função principal para resolver o problema
def color_map(mapa):
    estados = deque()
    estados.append(mapa)  # Começamos com o estado inicial (mapa vazio)

    while estados:
        estado_atual = estados.popleft()

        if is_solution(estado_atual):
            return estado_atual

        sucessores = generate_successors(estado_atual)
        estados.extend(sucessores)

    return None  # Se não encontrarmos uma solução, retornamos None

# Exemplo de uso:
mapa_inicial = criar_mapa()
solucao = color_map(mapa_inicial)

if solucao:
    print("Solução encontrada:")
    print(solucao)
else:
    print("Não foi possível encontrar uma solução.")
