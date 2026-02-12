# 11779
import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
lst = [[]for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    lst[s].append((e, w))

start, end = map(int, input().split())

# 다익스트라
d = [sys.maxsize]*(n+1)
hq = []

d[start] = 0
# 이전 경로 저장
rt = [0]*(n+1)
heapq.heappush(hq, (0, start))

while hq:
    weight, now = heapq.heappop(hq)

    # 더 짧은 경로를 이미 찾은 경우
    if d[now] < weight:
        continue

    for nxt, w in lst[now]:
        cost = weight + w
        if d[nxt] > cost:
            d[nxt] = cost
            rt[nxt] = now
            heapq.heappush(hq, (cost, nxt))

print(d[end])

ans = []
temp = end
while temp != 0:
    ans.insert(0, temp)
    temp = rt[temp]

print(len(ans))
print(*ans)