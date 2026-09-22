n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
ans=99999999
visited=[False]*n
def choose(lst, total):
    global ans

    if len(lst)==n:
        if A[lst[-1]][0]==0:
            return
        ans = min(ans, total+A[lst[-1]][0])
        return

    for i in range(n):
        if not visited[i] and A[lst[-1]][i]!=0:
            visited[i]=True
            lst.append(i)

            choose(lst, total+A[lst[-2]][i])

            visited[i]=False
            lst.pop()
visited[0]=True
plst=[0]
choose(plst, 0)
print(ans)