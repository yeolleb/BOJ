# 1644
# 현재는 O(N^2)에 가깝다
# -> 투포인터로 개선 가능
import sys, math
input = sys.stdin.readline
MAXSIZE = 4000000

n = int(input())

prime = [True]*(MAXSIZE+1)
prime[0] = False
prime[1] = False

for i in range(2, int(math.sqrt(MAXSIZE))+1):
    if prime[i]:
        for j in range(i+i, MAXSIZE+1, i):
            prime[j] = False

# 프라임 리스트
plst = []
for i in range(2, MAXSIZE+1):
    if prime[i]:
        plst.append(i)

length = len(plst)
ans = 0

for i in range(length):
    cnt = i
    now = plst[cnt]
    while cnt < length and now <= n:
        if now == n:
            ans += 1
        cnt += 1
        if cnt < length-1:
            now += plst[cnt]

print(ans)