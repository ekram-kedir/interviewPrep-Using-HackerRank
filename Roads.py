from collections import defaultdict
length = int(input())
count = 0
graph = defaultdict(list)
adjacencyMatrix = []
for row in range(length):
    rows = list(map(int,input().split()))
    adjacencyMatrix.append(rows)

for row in range(length):
    for col in range(length):
        if row != col and adjacencyMatrix[row][col]:
            count += 1

print(count//2)
