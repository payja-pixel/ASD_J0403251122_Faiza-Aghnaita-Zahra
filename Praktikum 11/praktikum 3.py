# =========================================================================
# Nama  : Faiza Aghnaita Zahra
# NIM   : J0403251122
# Kelas : TPL A2/P2
# Praktikum 3 - Konversi matrix ke list
# =========================================================================

matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]

nodes = ["A", "B", "C", "D"]
graph = {}

for i in range(len(matrix)):
    graph[nodes[i]] = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[nodes[i]].append(nodes[j])

print("Adjacency List:")

for node in graph:
    print(node, "->", graph[node])