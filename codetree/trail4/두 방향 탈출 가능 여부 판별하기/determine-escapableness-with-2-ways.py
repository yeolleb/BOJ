n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

visited = [[False for _ in range(m)]for __ in range(n)]
isSolved = False

def dfs(x, y):
    global isSolved

    if x == n-1 and y == m-1:
        isSolved = True
        return

    for k in range(2):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                dfs(nx, ny)

visited[0][0] = True
dfs(0, 0)
if isSolved:
    print(1)
else:
    print(0)