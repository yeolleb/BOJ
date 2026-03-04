# 9466
# 또 재귀,,,, 재귀는 어려워...
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(v):
    visited[v] = 1
    nxt = lst[v]

    if visited[nxt] == 1:
        cur = nxt
        team.add(cur)

        while cur != v:
            cur = lst[cur]
            team.add(cur)
    
    elif visited[nxt] == 0:
        dfs(nxt)
    
    visited[v] = 2

t = int(input())
for _ in range(t):
    n = int(input())
    lst = [0] + list(map(int, input().split()))

    visited = [0]*(n+1)
    team = set()

    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)
    
    print(n - len(team))