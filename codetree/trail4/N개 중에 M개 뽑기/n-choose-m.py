N, M = map(int, input().split())

def dfs(lst, k):
    if len(lst) == M:
        print(*lst)
        return

    for nk in range(k+1, N+1):
        lst.append(nk)
        dfs(lst, nk)
        lst.pop()

for i in range(1, N+1):
    plst = [i]
    dfs(plst, i)