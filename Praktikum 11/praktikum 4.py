# =========================================================================
# Nama  : Faiza Aghnaita Zahra
# NIM   : J0403251122
# Kelas : TPL A2/P2
# Praktikum 4 - Studi kasus dunia nyata (Media Sosial)
# =========================================================================

# Adjacency List 
graph = {
    "Faiza": ["Nayla", "Cantik"],
    "Nayla": ["Intan", "Haura"],
    "Cantik": ["Intan"],
    "Intan": ["Haura"],
    "Haura": ["Faiza"]
}

print("Adjacency List:")

for node in graph:
    print(node, "->", graph[node])

# Adjacency Matrix
# Urutan Node
nodes = ["Faiza", "Nayla", "Cantik", "Intan", "Haura"]
matrix = [
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,0,0,1,0],
    [0,0,0,0,1],
    [1,0,0,0,0]
]


print("\nUrutan Node:")
print(nodes)
print("\nAdjacency Matrix:")
for row in matrix:
    print(row)