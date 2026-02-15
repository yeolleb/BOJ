# 162368
# 첫 아기 상어 크기 = 2
# 한번에 bfs 말고 먹을 수 있는 위치 마다 bfs 돌리기
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

fish = set()

for i in range(n):
    for j in range(n):
        if lst[i][j] == 9:
            rx = i
            ry = j
        elif lst[i][j] > 0:
            fish.add((i, j))

def bfs(fx, fy, size):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = [[False for _ in range(n)]for __ in range(n)]
    dq = deque()

    dq.append((fx, fy, 0))

    while dq:
        x, y, cnt = dq.popleft()

        if 1<=lst[x][y]<=6:
            if (x, y) in fish:
                fish.remove((x, y))
                return (x, y, cnt)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny, cnt+1))
    
    return (0, 0, -1)

ans = 0
siz = 2
while fish:
    rx, ry, tmp = bfs(rx, ry, siz)
    ans += tmp
    siz += 1
print(ans)