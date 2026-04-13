# 16946
# 발상의 전환: 탐색의 시작점을 1이 아니라 0으로 지정.
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().strip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

walls = []
gid_lst = [[0 for _ in range(m)]for __ in range(n)]
gdict = dict()
dq = deque()
visited = [[False for _ in range(m)]for __ in range(n)]

nowgid = 1
for i in range(n):
    for j in range(m):
        if lst[i][j] > 0:
            walls.append((i, j))

        elif lst[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            gid_lst[i][j] = nowgid
            nowsize = 1
            dq.append((i, j))

            while dq:
                x, y = dq.popleft()

                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]

                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and lst[nx][ny] == 0:
                        visited[nx][ny] = True
                        gid_lst[nx][ny] = nowgid
                        nowsize += 1
                        dq.append((nx, ny))
            gdict[nowgid] = nowsize
            nowgid += 1

for x, y in walls:
    visited_gid = set()

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]

        if 0<=nx<n and 0<=ny<m and lst[nx][ny] == 0 and gid_lst[nx][ny] not in visited_gid:
            visited_gid.add(gid_lst[nx][ny])
            lst[x][y] += gdict[gid_lst[nx][ny]]

for i in range(n):
    for j in range(m):
        print(lst[i][j]%10, end="")
    print()