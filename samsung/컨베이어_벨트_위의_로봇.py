# 20055
# pypy3
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = n-1
dur = 0
lev = 0
robots = [False]*n

while True:
    if dur >= k:
        print(lev)
        break
    
    # 단계
    lev += 1
    # 1. 벨트 회전
    l = (l-1)%(2*n)
    r = (r-1)%(2*n)

    for i in range(n-1, 0, -1):
        if not robots[i] and robots[i-1]:
            robots[i] = True
            robots[i-1] = False
    
    # 내리는 위치 즉시 내리기
    if robots[n-1]:
        robots[n-1] = False
    
    # 2. 로봇 한칸 이동
    for i in range(n-1, 0, -1):
        if not robots[i] and robots[i-1] and a[(l+i)%(2*n)] > 0:
            robots[i] = True
            robots[i-1] = False
            a[(l+i)%(2*n)] -= 1
            if a[(l+i)%(2*n)] == 0:
                dur += 1
    
    # 내리는 위치 즉시 내리기
    if robots[n-1]:
        robots[n-1] = False
    
    # 3. 로봇 올리기
    if a[l] > 0:
        robots[0] = True
        a[l] -= 1
        if a[l] == 0:
            dur += 1