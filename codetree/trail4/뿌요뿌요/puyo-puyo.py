import sys

input = sys.stdin.readline

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

exploded = 0
max_size = 0


def dfs(x, y):
    visited[x][y] = True
    size = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                size += dfs(nx, ny)

    return size


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            size = dfs(i, j)

            if size >= 4:
                exploded += 1

            max_size = max(max_size, size)

print(exploded, max_size)