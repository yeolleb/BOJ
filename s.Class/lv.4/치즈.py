# 2638
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# bfs
def find_air():
    visited = [[False for _ in range(m)]for __ in range(n)]
    dq = deque()

    # 모눈종이의 맨 가장자리에는 치즈가 놓이지 않음
    air = set()
    air.add((0, 0))
    dq.append((0, 0))
    visited[0][0] = True

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and lst[nx][ny] == 0:
                    air.add((nx, ny))
                    dq.append((nx, ny))
                    visited[nx][ny] = True
    return air

chz = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            chz.append((i, j))

time = 0
while chz:
    time += 1
    air = find_air()

    # 여전히 치즈인 리스트
    temp = []
    # 사라질 치즈 리스트
    dis = []

    for x, y in chz:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in air:
                cnt += 1
        # 2변 이상 접촉 (사라질 치즈)
        if cnt >= 2:
            dis.append((x, y))
        # 남는 치즈
        else:
            temp.append((x, y))
    
    chz = temp
    for x, y in dis:
        lst[x][y] = 0

print(time)