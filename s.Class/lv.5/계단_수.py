# 1562
import sys
input = sys.stdin.readline

n = int(input())
MOD = 10**9
# dp[N번째 수][마지막 수][방문한 수 bitmasking(0~1023)]
dp = [[[0 for _ in range(1 << 10)]for _ in range(10)]for _ in range(n+1)]

for j in range(1, 10):
    dp[1][j][1 << j] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(1 << 10):
            new_mask = k | 1 << j

            if j == 0:
                dp[i][j][new_mask] += dp[i-1][j+1][k] % MOD
            elif j == 9:
                dp[i][j][new_mask] += dp[i-1][j-1][k] % MOD
            else:
                dp[i][j][new_mask] += dp[i-1][j+1][k] % MOD + dp[i-1][j-1][k] % MOD

ans = 0
for j in range(10):
    ans += dp[n][j][1023]

print(ans % MOD)