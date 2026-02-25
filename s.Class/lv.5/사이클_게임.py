# 20040
# 첫 풀이(dfs, 백트래킹): 예제는 다 맞았으나 시간초과 O(NM)
# 사이클 -> 유니온 파인드 생각해내기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    ap = find(a)
    bp = find(b)

    if ap != bp:
        parent[bp] = ap
        return False
    else:
        return True

n, m = map(int, input().split())
parent = [i for i in range(n)]
lst = [[]for _ in range(n)]
ans = 0

for times in range(1, m+1):
    a, b = map(int, input().split())

    if union(a, b):
        ans = times
        break

print(ans)