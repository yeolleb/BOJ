# 1647
# 최소 신장 트리(mst): 사이클 x, n-1개 엣지
# -> 엣지 리스트, 유니온 파인드 리스트, 힙큐로 구현
# 현재 문제에서 두개로 나눠야하니 n-2개 엣지로 만들기
import sys, heapq
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, (c, a, b))

def find(v):
    if v == parent[v]:
        return v
    
    parent[v] = find(parent[v])
    return parent[v]

def union(s, e):
    sp = find(s)
    ep = find(e)

    if sp != ep:
        parent[ep] = sp

ans = 0
cnt = 0
while edges:
    if cnt == n-2:
        break

    w, s, e = heapq.heappop(edges)
    sp = find(s)
    ep = find(e)

    # 사이클 방지
    if sp != ep:
        union(s, e)
        ans += w
        cnt += 1

print(ans)