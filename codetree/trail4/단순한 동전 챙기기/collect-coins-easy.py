from collections import deque

n = int(input())
grid = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            sx = i
            sy = j

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# visited[마지막 동전 번호][x][y][동전 개수]
visited = [[[[False for _ in range(4)]for __ in range(n)]for ___ in range(n)]for ____ in range(10)]
dq = deque()
lst = []

visited[0][sx][sy][0] = True
# x, y, 마지막으로 주운 동전 번호, 동전 개수, 이동 횟수
dq.append((sx, sy, 0, 0, 0))

while dq:
    x, y, last, cnt, dist = dq.popleft()

    # 동전 3개 이상 모으고 E 도착
    if len(grid[x][y]) and grid[x][y] == 'E' and cnt >= 3:
        print(dist)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue

        # --------------------------------
        # 1. 그냥 지나가는 경우
        # --------------------------------
        if not visited[last][nx][ny][cnt]:
            visited[last][nx][ny][cnt] = True
            dq.append((nx, ny, last, cnt, dist + 1))

        # --------------------------------
        # 2. 동전을 줍는 경우
        # --------------------------------
        if grid[nx][ny].isdigit():
            coin = int(grid[nx][ny])

            # 번호가 증가해야만 주울 수 있음
            if coin > last:
                new_cnt = min(3, cnt + 1)

                if not visited[coin][nx][ny][new_cnt]:
                    visited[coin][nx][ny][new_cnt] = True
                    dq.append((nx, ny, coin, new_cnt, dist + 1))
else:
    print(-1)