
from collections import defaultdict

n, m = map(int, input().split())

cols = defaultdict(list)
rows = defaultdict(list)
grid = []
answer = ""

for _ in range(n):
    row = list(input().strip())
    grid.append(row)

for i in range(n):
    for j in range(m):
        rows[i + 1].append(grid[i][j])
        cols[j + 1].append(grid[i][j])

for row in range(n):
    for col in range(m):
        current = rows[row + 1] + cols[col + 1]
        find = grid[row][col]
        x = current.count(find)
        if x == 2:
            answer += find
print(answer)
