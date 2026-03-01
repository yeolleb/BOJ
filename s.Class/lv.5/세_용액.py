# 2473
# pypy3
# 하나는 고정, 나머지 투포인터로 이동
# 바깥 루프 → N
# 안쪽 투포인터 → N (다시 되돌아가서 탐색하지 않기 때문에, 움직이는 총 횟수는 최대 N)
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
result = sys.maxsize

for i in range(n-2):
    if result == 0:
        break
    
    l = i+1
    r = n-1

    while l < r:
        tmp = abs(lst[i] + lst[l] + lst[r])
        if result > tmp:
            result = tmp
            ans = [lst[i], lst[l], lst[r]]
        
        if lst[i] + lst[l] + lst[r] > 0:
            r -= 1
        else:
            l += 1

print(*ans)