# 14503
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, dir):
    global cnt
    
    # 청소할 공간 O
    for i in range(1, 5):
        nd = (dir-i)%4
        nx = x+dx[nd]
        ny = y+dy[nd]
        if 0<=nx<n and 0<=ny<m and lst[nx][ny] == 0 and not visited[nx][ny]:
           visited[nx][ny] = True
           cnt += 1
           return dfs(nx, ny, nd)
    
    # 청소할 공간 X
    nx = x-dx[dir]
    ny = y-dy[dir]
    if 0<=nx<n and 0<=ny<m and lst[nx][ny] == 0:
        return dfs(nx, ny, dir)

visited = [[False for _ in range(m)]for __ in range(n)]
cnt = 1
visited[r][c] = True
dfs(r, c, d)

print(cnt)