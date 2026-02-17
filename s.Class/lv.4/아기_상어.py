# 16236
# 첫 아기 상어 크기 = 2
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
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
    candidates = []
    min_cnt = sys.maxsize

    dq.append((fx, fy, 0))
    visited[fx][fy] = True

    while dq:
        x, y, cnt = dq.popleft()

        if 1<=lst[x][y]<=6:
            if size > lst[x][y] and (x, y) in fish and cnt <= min_cnt:
                min_cnt = cnt
                candidates.append((x, y))

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if lst[nx][ny] == 9 or size >= lst[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx, ny, cnt+1))
    
    if candidates:
        candidates.sort(key=lambda x: (x[0], x[1]))
        x = candidates[0][0]
        y = candidates[0][1]
        fish.remove((x, y))
        return (x, y, min_cnt)
    return (0, 0, -1)

ans = 0
siz = 2
xp = 0
while fish:
    rx, ry, tmp = bfs(rx, ry, siz)
    if tmp == -1:
        break
    ans += tmp
    xp += 1
    if siz == xp:
        siz += 1
        xp = 0
print(ans)