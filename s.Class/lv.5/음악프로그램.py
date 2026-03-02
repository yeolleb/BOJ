# 2623
# 순서를 정하라 -> 위상정렬
# 위상정렬 -> indegree, cycle X, 방향 리스트, deque
# indegree = 진입 차수 리스트: 자기 자신을 가리키는 엣지의 개수
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[]for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        lst[tmp[i]].append(tmp[i+1])
        indegree[tmp[i+1]] += 1

dq = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)

ans = []
while dq:
    now = dq.popleft()
    ans.append(now)

    for nxt in lst[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            dq.append(nxt)

if len(ans) < n:
    print(0)
else:
    for i in ans:
        print(i)