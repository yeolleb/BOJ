n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

col_visited=[False]*n

ans=0

def choose(row, tmp):
    global ans

    if row==n:
        ans=max(ans, tmp)
        return

    for i in range(n):
        if not col_visited[i]:
            col_visited[i]=True

            choose(row+1, min(tmp, grid[row][i]))

            col_visited[i]=False

choose(0, 99999)
print(ans)