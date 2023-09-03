from graphviz import Digraph

# Defina seu mapa
mapa = {
    'Home': {'Museum': 2.7, 'Club': 1.2, 'Bank': 1.3},
    'Museum': {'Park': 1.6, 'Bank': 1.7},
    'Park': {'Lake': 1.6, 'Bank': 1.8},
    'Lake': {'School': 0.9},
    'School': {'Club': 1.4, 'Bank': 1},
    'Bank': {'Club': 1.1, 'Lake': 1}
}

# Crie um gráfico
graph = Digraph(format='png')

# Adicione nós ao gráfico
for local in mapa:
    graph.node(local)

# Adicione arestas bidirecionais ao gráfico com as distâncias como rótulos
for origem, conexoes in mapa.items():
    for destino, distancia in conexoes.items():
        # Adicione setas bidirecionais com as distâncias como rótulos
        graph.edge(origem, destino, label=f'{distancia} km', dir='both')

# Renderize o gráfico em um arquivo
graph.render('mapa_bidirecional')
