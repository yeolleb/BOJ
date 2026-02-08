# 1238
import sys, heapq
input = sys.stdin.readline
n, m, x = map(int, input().split())
org_lst = [[]for _ in range(n+1)]
rev_lst = [[]for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    org_lst[s].append((e, w))
    rev_lst[e].append((s, w))

def dijkstra(s, lst):
    d = [sys.maxsize]*(n+1)
    hq = []

    heapq.heappush(hq, (0, s))
    d[s] = 0

    while hq:
        weight, now = heapq.heappop(hq)

        # 더 짧은 경로를 이미 찾은 경우
        if d[now] < weight:
            continue
        
        for nxt, tw in lst[now]:
            nxtw = weight + tw
            if nxtw < d[nxt]:
                d[nxt] = nxtw
                heapq.heappush(hq, (nxtw, nxt))
    return d

# 1. 파티에서 집으로 돌아오는 최단 거리 (X -> 각 마을)
come_back = dijkstra(x, org_lst)

# 2. 집에서 파티로 가는 최단 거리 (X <- 각 마을)
go_party = dijkstra(x, rev_lst)

ans = 0
for i in range(1, n+1):
    temp = go_party[i] + come_back[i]
    if ans < temp:
        ans = temp

print(ans)