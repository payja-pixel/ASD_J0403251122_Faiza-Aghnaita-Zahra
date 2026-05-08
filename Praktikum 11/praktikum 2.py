# =========================================================================
# Nama  : Faiza Aghnaita Zahra
# NIM   : J0403251122
# Kelas : TPL A2/P2
# Praktikum 2 - Adjacency List
# =========================================================================

graph = {}

def add_edge(node1, node2):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)

def print_graph():
    for node in graph:
        print(node, "->", graph[node])

# membuat edge
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "C")
add_edge("B", "D")
add_edge("C", "D")

print("Adjacency List:")
print_graph()