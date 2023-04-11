from collections import defaultdict
length = int(input())

graph = defaultdict(list)
adjacencyMatrix = []
for row in range(length):
    rows = list(map(int,input().split()))
    adjacencyMatrix.append(rows)

for row in range(length):
    for col in range(length):
        if row != col and adjacencyMatrix[row][col]:
            graph[row + 1].append(col + 1)

for k, v in graph.items():
    print(len(v),*v)
