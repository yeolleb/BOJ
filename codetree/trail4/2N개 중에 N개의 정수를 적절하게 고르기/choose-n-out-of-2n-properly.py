from itertools import combinations
import sys

n = int(input())
num = list(map(int, input().split()))

ans = sys.maxsize

# 조합의 절반으로 자르는 것 = 첫 번째 원소를 반드시 뽑는다.
# -> 숫자 중복 허용이면 이게 안됨. 인덱스로 해야됨.
for i in combinations(range(2 * n), n):
    if 0 not in i:
        continue

    j = [x for x in range(2 * n) if x not in i]

    sum_i = sum(num[x] for x in i)
    sum_j = sum(num[x] for x in j)

    ans = min(ans, abs(sum_i - sum_j))

print(ans)