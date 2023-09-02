import graphviz

# Definindo a estrutura da árvore como um dicionário
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

# Criar um objeto Graphviz
dot = graphviz.Digraph(format='png')

# Adicionar nós e arestas ao objeto Graphviz
for node, children in tree.items():
    dot.node(str(node))
    for child in children:
        dot.edge(str(node), str(child))

# Salvar o diagrama em um arquivo e renderizá-lo
dot.render('arvore')

# O diagrama será salvo como 'arvore.png' no diretório atual.
