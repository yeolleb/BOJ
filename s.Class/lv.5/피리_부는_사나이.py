# 16724
# 사이클 몇개 있는지 찾으면 될듯
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(input().strip()))

def cal_nxt(r, c, dir):
    if dir == 'U':
        return r-1, c
    elif dir == 'D':
        return r+1, c
    elif dir == 'R':
        return r, c+1
    elif dir == 'L':
        return r, c-1

def dfs(r, c):
    isNew = True
    if visited[r][c] == 0:
        visited[r][c] = 1
        nxtr, nxtc = cal_nxt(r, c, lst[r][c])
        if not dfs(nxtr, nxtc):
            isNew = False
    # elif visited[r][c] == 1:
    #     # +1개
    elif visited[r][c] == 2:
        # 원래 있던 사이클이라 계산X
        isNew = False
    visited[r][c] = 2
    if isNew:
        return True
    else:
        return False

# 방문X(0), 탐색중(1), 탐색완료(2)
visited = [[0 for _ in range(m)]for __ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j):
                ans += 1

print(ans)