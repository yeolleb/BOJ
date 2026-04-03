# 28707
# 리스트를 튜플로 전환하면 딕셔너리의 키로 전환할 수 있다 !!
# 첨엔 m가지 수를 다 써봐야한다고 생각했다. 근데 최소 비용이니 BFS를 떠올렸다.
# 이때 visited 처리를 어떻게 해야하는지 헤맸는데 list를 tuple로 전환하여 해결.
import sys, heapq
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
op = []

for _ in range(m):
    l, r, c = map(int, input().split())
    op.append((l-1, r-1, c))

sucess = [0]*n
for i in range(n):
    sucess[i] = a[i]
sucess.sort()
isSuccess = False

visited = dict()
hq = []

visited[tuple(a)] = 0
heapq.heappush(hq, (0, a))

while hq:
    cost, lst = heapq.heappop(hq)

    if lst == sucess:
        isSuccess = True
        print(cost)
        break

    for l, r, c in op:
        tmplst = [0]*n
        for i in range(n):
            tmplst[i] = lst[i]
        tmp = tmplst[l]
        tmplst[l] = tmplst[r]
        tmplst[r] = tmp

        tmpTuple = tuple(tmplst)
        nxtC = cost + c

        if tmpTuple in visited:
            if visited[tmpTuple] <= nxtC:
                continue
        
        visited[tmpTuple] = nxtC
        heapq.heappush(hq, (nxtC, tmplst))

if not isSuccess:
    print(-1)