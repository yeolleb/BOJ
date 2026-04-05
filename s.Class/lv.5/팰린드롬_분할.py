# 1509
# dp[i] = ~i까지 최소 팰린드롬 개수
# 0~i-1까지 k 돌면서 k+1~i까지 팰린드롬이면 dp[i] = dp[k] + 1
# isPalindrome[i][j] = i~j가 팰린드롬 true/false
# -> lst[i] == lst[j] and isPalindrome[i+1][j-1] == true 이면 true
import sys
input = sys.stdin.readline

lst = list(input().strip())

n = len(lst)
isPalindrome = [[False for _ in range(n)]for __ in range(n)]

for i in range(n):
    isPalindrome[i][i] = True

for i in range(n-1):
    if lst[i] == lst[i+1]:
        isPalindrome[i][i+1] = True

for length in range(2, n):
    for i in range(n):
        if i+length < n and lst[i] == lst[i+length] and isPalindrome[i+1][i+length-1]:
            isPalindrome[i][i+length] = True

dp = [sys.maxsize]*n

for i in range(n):
    if isPalindrome[0][i]:
        dp[i] = 1
        continue
    for k in range(i):
        if isPalindrome[k+1][i]:
            dp[i] = min(dp[i], dp[k]+1)

print(dp[n-1])