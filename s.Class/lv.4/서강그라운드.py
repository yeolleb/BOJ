# 14938
# 다익스트라는 우선순위 큐 !
# + visited를 pop 시점에 처리 !
# 다익스트라 vs 플로이드 워셜 차이점?
import sys, heapq
input = sys.stdin.readline
n, m, r = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
myList = [[]for _ in range(n+1)]
for _ in range(r):
    s, e, w = map(int, input().split())
    myList[s].append((e, w))
    myList[e].append((s, w))

ans = 0
for i in range(1, n+1):
    visited = [False]*(n+1)
    q = []
    heapq.heappush(q, (0, i))
    temp = 0

    while q:
        weight, node = heapq.heappop(q)
        
        if visited[node]:
            continue
        visited[node] = True

        temp += a[node]

        for nn, nw in myList[node]:
            tw = weight + nw
            if tw <= m:
                heapq.heappush(q, (tw, nn))

    ans = max(ans, temp)

print(ans)