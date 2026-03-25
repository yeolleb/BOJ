# 1766
# 위상정렬로 다시 풀기
import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
child = [[]for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    child[a].append(b)
    indegree[b] += 1

hq = []
ans = []

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)

while hq:
    v = heapq.heappop(hq)
    ans.append(v)

    for c in child[v]:
        indegree[c] -= 1
        if indegree[c] == 0:
            heapq.heappush(hq, c)

print(*ans)