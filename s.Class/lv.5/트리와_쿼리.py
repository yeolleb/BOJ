# 15681
import sys
from collections import deque
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
n, r, q = map(int, input().split())
lst = [[]for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

# make tree
child = [[]for _ in range(n+1)]

dq = deque()
dq.append(r)

while dq:
    node = dq.popleft()
    for nxt in lst[node]:
        if not child[nxt]:
            child[node].append(nxt)
            dq.append(nxt)

# 재귀
def count(node):
    cnt = 1
    for nxt in child[node]:
        cnt += count(nxt)
    ans[node] = cnt
    return cnt

ans = [1]*(n+1)
count(r)

for _ in range(q):
    u = int(input())
    print(ans[u])