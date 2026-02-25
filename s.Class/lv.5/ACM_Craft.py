# 1005
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def sol(v):
    # 이미 계산한 경우
    if ans[v] != -1:
        return ans[v]
    
    time = d[v]
    tmp = [0]

    for prev in lst[v]:
        tmp.append(sol(prev))
    
    time += max(tmp)
    ans[v] = time
    return time

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    lst = [[]for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split())
        lst[y].append(x)

    w = int(input())

    ans = [-1]*(n+1)
    
    print(sol(w))