from collections import defaultdict
length = int(input())
outdegree =  defaultdict(int)
indegree = defaultdict(int)
adjacencyMatrix = []
for row in range(length):
    rows = list(map(int,input().split()))
    adjacencyMatrix.append(rows)

for row in range(length):
    for col in range(length):
        if row != col and adjacencyMatrix[row][col]:
            indegree[col + 1] = row + 1
            outdegree[row + 1] = col + 1

source = []
sink = []

for val in range(length):
    if not indegree[val + 1]:
        source.append(val + 1)
    if not outdegree[val + 1]:
        sink.append(val + 1)

print(len(source),*source)
print(len(sink),*sink)
