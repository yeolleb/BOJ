from itertools import combinations
import sys

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize

for i in combinations(range(n), m):
    temp = 0
    for j in range(m-1):
        a, b = points[i[j]]
        for l in range(j, m):
            c, d = points[i[l]]
            temp = max(temp, (a-c)**2+(b-d)**2)
    ans = min(ans, temp)

print(ans)