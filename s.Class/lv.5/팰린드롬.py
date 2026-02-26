# 10942
import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
m = int(input())

dp = [[0 for _ in range(n+1)]for __ in range(n+1)]

# ** 길이 순서대로 dp 채우기 **
# 길이 1
for i in range(1, n+1):
    dp[i][i] = 1

# 길이 2
for i in range(1, n):
    if num[i] == num[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상
for length in range(3, n+1):
    # 최대 길이 가능한 모든 인덱스
    for i in range(1, n+2-length):
        # 첫번째와 마지막 숫자 같은지
        if num[i] == num[i+length-1]:
            # 그 사이 dp == 1인지
            if dp[i+1][i+length-2] == 1:
                dp[i][i+length-1] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])