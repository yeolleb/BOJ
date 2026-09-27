n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False for _ in range(n)]for __ in range(n)]
lst = []

def dfs(x, y):
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and grid[nx][ny]==1:
                lst[-1]+=1
                visited[nx][ny]=True
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]==1:
            lst.append(1)
            visited[i][j]=True
            dfs(i, j)

lst.sort()
print(len(lst))
for ans in lst:
    print(ans)