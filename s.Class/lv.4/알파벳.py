# 1987
# set -> 시간초과
# 알파벳 = 26가지이므로 비트마스킹
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
r, c = map(int, input().split())
ml = []
for _ in range(r):
    ml.append(list(input().strip()))

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(i, j, cnt):
    global ans
    ans = max(ans, cnt)

    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]

        if x < 0 or y < 0 or x >= r or y >= c:
            continue

        bit = ord(ml[x][y])-65

        if visited[bit] == 0:
            visited[bit] = 1
            dfs(x, y, cnt+1)
            visited[bit] = 0

ans = 0
visited = [0]*26
visited[ord(ml[0][0])-65] = 1

dfs(0, 0, 1)

print(ans)