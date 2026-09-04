edges = [
    (0, 1),  # 0 → 1
    (0, 2),  # 0 → 2
    (1, 3),  # 1 → 3
]
graph = dict()

for i, j in edges:
    graph.setdefault(i, []).append(j)

print(graph)