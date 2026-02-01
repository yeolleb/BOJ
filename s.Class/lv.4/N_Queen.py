# 9663
# pypy3
# n*n, n개의 퀸 -> 무조건 한 row당 하나의 퀸
# 나머지 열, 대각선1, 대각선2 각각 visited 체크
# ↘ 대각선(d1) = row + col
# ↗ 대각선(d2) = row - col
import sys
input = sys.stdin.readline
n = int(input())

col = [False]*n
diag1 = [False]*(2*n-1)
diag2 = [False]*(2*n-1)
ans = 0

def check(tc, td1, td2, TF):
    col[tc] = TF
    diag1[td1] = TF
    diag2[td2] = TF

def dfs(row):
    global ans

    if row == n:
        ans += 1
        return
    
    for c in range(n):
        d1 = (row+c)
        d2 = row-c+n-1

        if not col[c] and not diag1[d1] and not diag2[d2]:
            check(c, d1, d2, True)
            dfs(row+1)
            check(c, d1, d2, False)

dfs(0)
print(ans)