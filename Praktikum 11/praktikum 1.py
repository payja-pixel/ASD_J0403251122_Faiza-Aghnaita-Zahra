# =========================================================================
# Nama  : Faiza Aghnaita Zahra
# NIM   : J0403251122
# Kelas : TPL A2/P2
# Praktikum 1 - Adjacency Matrix
# =========================================================================

V = 4 # jumlah vertex
matrix = [[0 for i in range(V)] for j in range(V)] # inisialisasi matriks adjacency dengan 0

def add_edge(i, j):
    matrix[i][j] = 1 # menandai adanya edge antara vertex i dan j
    matrix[j][i] = 1 # karena graph tidak berarah, maka matriks simetris

# membuat edge
add_edge(0, 1) # edge antara vertex 0 dan 1
add_edge(0, 2) # edge antara vertex 0 dan 2
add_edge(1, 2) # edge antara vertex 1 dan 2
add_edge(1, 3) # edge antara vertex 1 dan 3
add_edge(2, 3) # edge antara vertex 2 dan 3

print("Adjacency Matrix:")
for row in matrix:
    print(row)