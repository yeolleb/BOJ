# 14502
# 모든 경우의 수를 다루기 때문에 로직은 간단
# 거의 4중 for문 이지만 최대 n이 작다.
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
myList = []
for _ in range(n):
    myList.append(list(map(int, input().split())))

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if myList[i][j] == 0:
            empty.append((i, j))
        if myList[i][j] == 2:
            virus.append((i, j))

def bfs():
    # 우, 하, 좌, 상
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    visited = [[False for _ in range(m)]for __ in range(n)]
    dq = deque()

    for vx, vy in virus:
        visited[vx][vy] = True
        dq.append((vx, vy))

    while dq:
        now = dq.popleft()

        for k in range(4):
            nx = now[0]+dx[k]
            ny = now[1]+dy[k]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and myList[nx][ny] == 0:
                    visited[nx][ny] = True
                    dq.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and myList[i][j] == 0:
                cnt += 1
    return cnt

ans = []
for i in range(len(empty)-2):
    w1x, w1y = empty[i]
    myList[w1x][w1y] = 1
    for j in range(i+1, len(empty)-1):
        w2x, w2y = empty[j]
        myList[w2x][w2y] = 1
        for k in range(j+1, len(empty)):
            w3x, w3y = empty[k]
            myList[w3x][w3y] = 1
            ans.append(bfs())
            myList[w3x][w3y] = 0
        myList[w2x][w2y] = 0
    myList[w1x][w1y] = 0

print(max(ans))