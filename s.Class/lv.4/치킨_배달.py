# 15686
# 조합을 직접 백트래킹으로 구현 가능 (dfs 느낌)
import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

hm = []
chk = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            hm.append((i, j))
        if lst[i][j] == 2:
            chk.append((i, j))

def cal_chk_dist(chk_lst):
    dist = []
    for a, b in hm:
        d = sys.maxsize
        for p, q in chk_lst:
            temp = abs(a-p) + abs(b-q)
            d = min(d, temp)
        dist.append(d)
    return sum(dist)

ans = sys.maxsize
for comb in combinations(chk, m):
    ans = min(ans, cal_chk_dist(comb))

print(ans)