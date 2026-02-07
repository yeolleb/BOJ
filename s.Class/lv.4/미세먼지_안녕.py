# 17144
# bfs아니고 그냥 구현 문제... 살짝 노가다 느낌
import sys
from collections import deque
input = sys.stdin.readline
r, c, t = map(int, input().split())
a = [[0 for _ in range(c)]for __ in range(r)]
cle = []
dust = []

for i in range(r):
    row = list(map(int, input().split()))
    for j in range(c):
        if row[j] == -1:
            cle.append((i, j))
        
        if row[j] > 0:
            dust.append((i, j))
        
        a[i][j] = row[j]

# 먼지 확산
def spread():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    tmp = [[0 for _ in range(c)]for __ in range(r)]
    # 공기청정기 위치 유지
    for x, y in cle:
        tmp[x][y] = -1

    for i in range(r):
        for j in range(c):
            if a[i][j] <= 0:
                continue

            # 확산될 먼지
            w = a[i][j]//5
            cnt = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<r and 0<=ny<c and a[nx][ny] != -1:
                    tmp[nx][ny] += w
                    cnt += 1
            tmp[i][j] += a[i][j] - w * cnt
    return tmp

# 공기 청정기
def pur():
    # 반시계 방향 (뒤부터)
    row = cle[0][0]
    for i in range(row-1, 0, -1):
        a[i][0] = a[i-1][0]
    for j in range(c-1):
        a[0][j] = a[0][j+1]
    for i in range(row):
        a[i][c-1] = a[i+1][c-1]
    for j in range(c-1, 0, -1):
        a[row][j] = a[row][j-1]
    a[row][1] = 0

    # 시계 방향 (뒤부터)
    row = cle[1][0]
    for i in range(row+1, r-1):
        a[i][0] = a[i+1][0]
    for j in range(c-1):
        a[r-1][j] = a[r-1][j+1]
    for i in range(r-1, row, -1):
        a[i][c-1] = a[i-1][c-1]
    for j in range(c-1, 0, -1):
        a[row][j] = a[row][j-1]
    a[row][1] = 0

for _ in range(t):
    a = spread()
    pur()

ans = 0
for i in range(r):
    for j in range(c):
        if a[i][j] > 0:
            ans += a[i][j]
print(ans)