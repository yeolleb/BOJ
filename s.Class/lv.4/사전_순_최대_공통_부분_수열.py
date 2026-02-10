# 30805
# lcs로 풀라했는데 너무 복잡함
# 그냥 공통 부분 찾아서 가장 큰거 넣고
# 그 이후 남은거 없을 때 까지 반복
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

temp = set(a) & set(b)

ans = []
while temp:
    max_v = max(temp)
    ans.append(max_v)

    idx1 = a.index(max_v)
    idx2 = b.index(max_v)

    a = a[idx1+1:]
    b = b[idx2+1:]

    temp = set(a) & set(b)

print(len(ans))
print(*ans)