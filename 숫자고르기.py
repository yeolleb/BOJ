# 2668
# 유사 문제: 텀 프로젝트(9466)
# 사이클을 찾으라는 말을 문제 설명은 되게 어렵게 말함
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(v):
    visited[v] = 1
    nxt = lst[v]

    if visited[nxt] == 0:
        dfs(nxt)
    elif visited[nxt] == 1:
        cur = nxt
        ans.append(cur)

        while cur != v:
            cur = lst[cur]
            ans.append(cur)
    
    visited[v] = 2

n = int(input())
lst = [0]

for _ in range(n):
    lst.append(int(input()))

visited = [0]*(n+1)
ans = []

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)

ans.sort()

print(len(ans))
for i in ans:
    print(i)