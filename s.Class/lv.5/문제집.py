# 1766
# 그냥 구현으로 풀어버렸는데 위상정렬 문제였음.
import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [[]for _ in range(n+1)]
child = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    child[a].append(b)
    parent[b].append(a)

hq = []
ans = []

for i in range(1, n+1):
    # 부모 없으면 예비 리스트랑 비교 후 바로 출력
    if not parent[i]:
        while hq:
            if i < hq[0]:
                break
            else:
                v = heapq.heappop(hq)
                if not visited[v]:
                    visited[v] = True
                    ans.append(v)
                # 자식 있으면 우선순위 큐
                for c in child[v]:
                    isOK = True
                    for cp in parent[c]:
                        if not visited[cp]:
                            isOK = False
                            break
                    if isOK:
                        heapq.heappush(hq, c)
        if not visited[i]:
            visited[i] = True
            ans.append(i)
        # 자식 있으면 우선순위 큐
        for c in child[i]:
            isOK = True
            for cp in parent[c]:
                if not visited[cp]:
                    isOK = False
                    break
            if isOK:
                heapq.heappush(hq, c)

while hq:
    v = heapq.heappop(hq)
    if not visited[v]:
        visited[v] = True
        ans.append(v)
    # 자식 있으면 우선순위 큐
    for c in child[v]:
        isOK = True
        for cp in parent[c]:
            if not visited[cp]:
                isOK = False
                break
        if isOK:
            heapq.heappush(hq, c)

print(*ans)