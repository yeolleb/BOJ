# 13172
import sys
input = sys.stdin.readline
m = int(input())

X = 1000000007

# *빠른 거듭제곱*
# n^-1 = n^(x-2)  (mod x)
# v: 분모 e: 거듭제곱
def pow(v, e):
    if e == 0:
        return 1
    
    half = pow(v, e // 2)

    if e % 2 == 1:
        return (half * half * v) % X
    else:
        return (half * half) % X

ans = 0
for _ in range(m):
    n, s = map(int, input().split())
    ans += (pow(n, X-2) * s) % X

print(ans%X)