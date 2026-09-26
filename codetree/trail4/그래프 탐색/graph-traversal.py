n, m = map(int, input().split())
edges = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited=[False]*(n+1)
cnt = 0

def dfs(now):
    global cnt

    for next in edges[now]:
        if not visited[next]:
            visited[next]=True
            cnt+=1
            dfs(next)

visited[1]=True
dfs(1)
print(cnt)