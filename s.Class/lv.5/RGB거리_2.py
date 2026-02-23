# 17404
# 점화식은 1149와 동일
# + 처음 색깔 고를때 나머지 색깔은 고르지 못하도록 설정
# + 처음 색깔과 마지막 색깔이 같을 수 없도록 설정
# -> 기존 1149번에서 dp를 총 세번 돌린 것과 같다. 즉, 시간복잡도가 1149번의 3배
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
lst = []

for _ in range(n):
    r, g, b = map(int, input().split())
    lst.append((r, g, b))

ans = []
for k in range(3):
    dp = [[0 for _ in range(3)]for _ in range(n)]
    dp[0][k] = lst[0][k]
    dp[0][(k-1)%3] = sys.maxsize
    dp[0][(k+1)%3] = sys.maxsize

    for i in range(1, n):
        for j in range(3):
            dp[i][j] = lst[i][j] + min(dp[i-1][(j-1)%3], dp[i-1][(j+1)%3])
    
    # 마지막 색깔과 처음 색깔이 같을 수 없도록
    dp[n-1][k] = sys.maxsize
    
    ans.append(min(dp[n-1]))

print(min(ans))