# 10775
# 가능한 가장 큰 번호에 넣는게 유리
# find(x): 넣을 수 있는 가장 큰 번호 -> 타고가다가 자신과 동일할때가 가장 큰 번호. 최소는 0(도킹 불가)
# 넣을때마다 parent[find(x)] -= 1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
ans = 0

for _ in range(p):
    gate = int(input())
    real = find(gate)

    if real > 0:
        parent[real] -= 1
        ans += 1
    else:
        break

print(ans)