# 17070
# bfs는 시간초과
# dp로 풀어야함
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

# r, c: 파이프 끝 위치
#  dir: 0(가로), 1(세로), 2(대각선)
dp = [[[0 for _ in range(3)]for __ in range(n)]for ___ in range(n)]

# 시작: (0,1), 가로 방향
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            continue

        # →
        if j+1 < n and lst[i][j+1] != 1:
            # 직전에서 가로나 대각선이였다면 가로 가능
            dp[i][j+1][0] += dp[i][j][0]
            dp[i][j+1][0] += dp[i][j][2]

        # ↓
        if i+1 < n and lst[i+1][j] != 1:
            # 직전에서 세로나 대각선이였다면 세로 가능
            dp[i+1][j][1] += dp[i][j][1]
            dp[i+1][j][1] += dp[i][j][2]
        
        # ↘
        if i+1 < n and j+1 < n:
            if lst[i+1][j] != 1 and lst[i][j+1] != 1 and lst[i+1][j+1] != 1:
                # 직전 모든 방향에서 대각선 가능
                dp[i+1][j+1][2] += dp[i][j][0]
                dp[i+1][j+1][2] += dp[i][j][1]
                dp[i+1][j+1][2] += dp[i][j][2]

print(sum(dp[n-1][n-1]))

## bfs
# →, ↘, ↓
# dx = [0, 1, 1]
# dy = [1, 1, 0]

# dq = deque()
# dq.append((0, 0, 0, 1))

# ans = 0
# while dq:
#     a, b, c, d = dq.popleft()

#     if c == n-1 and d == n-1:
#         ans += 1
#         continue

#     row = c - a
#     col = d - b

#     # →
#     if row == 0 and col == 1:
#         for i in range(2):
#             e = c+dx[i]
#             f = d+dy[i]
#             if 0<=e<n and 0<=f<n and lst[e][f] != 1:
#                 if i == 1:
#                     if lst[e][f] == 1 or lst[e-1][f] == 1 or lst[e][f-1] == 1:
#                         continue
#                 dq.append((c, d, e, f))
#     # ↘
#     if row == 1 and col == 1:
#         for i in range(3):
#             e = c+dx[i]
#             f = d+dy[i]
#             if 0<=e<n and 0<=f<n and lst[e][f] != 1:
#                 if i == 1:
#                     if lst[e][f] == 1 or lst[e-1][f] == 1 or lst[e][f-1] == 1:
#                         continue
#                 dq.append((c, d, e, f))
#     # ↓
#     if row == 1 and col == 0:
#         for i in range(1, 3):
#             e = c+dx[i]
#             f = d+dy[i]
#             if 0<=e<n and 0<=f<n and lst[e][f] != 1:
#                 if i == 1:
#                     if lst[e][f] == 1 or lst[e-1][f] == 1 or lst[e][f-1] == 1:
#                         continue
#                 dq.append((c, d, e, f))

# print(ans)