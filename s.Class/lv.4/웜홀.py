# 1865
# 벨만포드, 음수사이클, 암기
import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())

    # 한 정점에서 시작하는 벨만포드와 다르게
    # 모든 정점에서 시작 가능하며, 음수 사이클 유무만 중요하기 때문에 초기값 0으로 설정
    d = [0]*(n+1)
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    # n-1번 업데이트
    for _ in range(n-1):
        for s, e, t in edges:
            if d[e] > d[s] + t:
                d[e] = d[s] + t
    
    mCycle = False
    for s, e, t in edges:
        if d[s] != sys.maxsize and d[e] > d[s] + t:
            mCycle = True

    if mCycle:
        print("YES")
    else:
        print("NO")