import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

maxk = 0
for i in range(n):
    for j in range(m):
        maxk = max(maxk, grid[i][j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, k):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and grid[nx][ny] > k:
                visited[nx][ny] = True
                dfs(nx, ny, k)

ans = (1, 0)

for nowk in range(1, maxk+1):
    visited = [[False for _ in range(m)]for __ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > nowk:
                tmp += 1
                visited[i][j] = True
                dfs(i, j, nowk)
    if ans[1] < tmp:
        ans = (nowk, tmp)

print(*ans)