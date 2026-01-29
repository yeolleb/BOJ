# 12851
# BFS에서 처음 방문한 노드는 항상 최단거리
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

visited = [-1]*100001
cnt = [0]*100001
dq = deque()

dq.append(n)
visited[n] = 0
cnt[n] = 1

while dq:
    now = dq.popleft()

    for next in now-1, now+1, now*2:
        if 0 <= next <= 100000:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                cnt[next] = cnt[now]
                dq.append(next)
            # 같은 최단 시간으로 재방문
            elif visited[next] == visited[now] + 1:
                cnt[next] += cnt[now]

print(visited[k])
print(cnt[k])