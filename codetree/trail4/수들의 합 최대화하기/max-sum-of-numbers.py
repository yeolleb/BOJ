n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

col_visited = [False]*n

ans = 0

# 행 순서대로 보면서 열 선택하기.
def choose(row, total):
    global ans

    if row == n:
        ans = max(ans, total)
        return

    for j in range(n):
        if not col_visited[j]:
            col_visited[j] = True

            choose(row+1, total+grid[row][j])

            col_visited[j] = False

choose(0, 0)

print(ans)