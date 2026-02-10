# 2206
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().strip())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[[False for _ in range(2)]for __ in range(m)]for ___ in range(n)]

dq = deque()
dq.append((0, 0, 1, 0))
visited[0][0][0] = False

isFail = True
while dq:
    x, y, d, c = dq.popleft()

    if x == n-1 and y == m-1:
        print(d)
        isFail = False
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny][c]:
            if lst[nx][ny] == 0:
                visited[nx][ny][c] = True
                dq.append((nx, ny, d+1, c))
                
            if lst[nx][ny] == 1 and c == 0:
                visited[nx][ny][c+1] == True
                dq.append((nx, ny, d+1, c+1))

if isFail:
    print(-1)