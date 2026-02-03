# 14500
# https://jominseoo.tistory.com/96
import sys
sys.setrecursionlimit(1000000) # pypy3에서 메모리 초과 발생
input = sys.stdin.readline
n, m = map(int, input().split())
myList = []

for _ in range(n):
    myList.append(list(map(int, input().split())))

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False for _ in range(m)]for __ in range(n)]

# mx: 가장 큰 값
mx = -1
for i in range(n):
    for j in range(m):
        mx = max(mx, myList[i][j])

def dfs(t, cnt, lst):
    global ans

    # 가지치기
    # 남은 칸 전부가 mx여도 ans 못 넘으면 더 볼 필요 없음
    if t + (4-cnt)*mx <= ans:
        return

    if cnt == 4:
        ans = max(ans, t)
        return

    # 지금까지 선택한 모든 칸(lst)에 대해 확장
    for lx,ly in lst:
        for i in range(4):
            x = lx + dx[i]
            y = ly + dy[i]
            if 0<=x<n and 0<=y<m:
                if not visited[x][y]:
                    visited[x][y] = True
                    dfs(t+myList[x][y], cnt+1, lst+[(x, y)])
                    visited[x][y] = False

ans = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(myList[i][j], 1, [(i, j)])

print(ans)