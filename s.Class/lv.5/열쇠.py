# 9328
# 알파벳 26개 비트마스킹은 너무 크다...
# -> 문을 못 열면 위치를 저장해둔다, 키를 먹으면 그 문들을 다시 BFS에 넣는다
# 소문자 = 97 ~ 122
# 대문자 = 65 ~ 90
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    mlst = []
    h, w = map(int, input().split())

    for _ in range(h):
        mlst.append(list(input().strip()))

    # 키를 -97해서 집합으로 저장
    klst = list(input().strip())
    keys = set()
    for k in klst:
        if k == '0':
            break
        keys.add(ord(k)-97)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False for __ in range(w)]for ___ in range(h)]
    dq = deque()

    # 출입구 찾기
    start = []
    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w):
                if mlst[i][j] != '*':
                    visited[i][j] = True
                    dq.append((i, j))
        else:
            for j in 0, w-1:
                if mlst[i][j] != '*':
                    visited[i][j] = True
                    dq.append((i, j))

    # 문서 찾기
    docs = set()
    for i in range(h):
        for j in range(w):
            if mlst[i][j] == '$':
                docs.add((i, j))
    docs_cnt = len(docs)

    # 잠긴 문은 집합으로 보관
    locked = set()

    while dq and docs:
        x, y = dq.popleft()

        # 문서
        if mlst[x][y] == '$':
            if (x, y) in docs:
                docs.remove((x, y))
            else:
                continue
        
        # 대문자
        if 65 <= ord(mlst[x][y]) <= 90:
            if ord(mlst[x][y])-65 not in keys:
                visited[x][y] = True
                locked.add((x, y))
                continue

        # 소문자
        if 97 <= ord(mlst[x][y]) <= 122:
            tk = ord(mlst[x][y])-97
            keys.add(tk)
            # 키 획득 할 경우 못갔던 방 다시 방문
            erase = []
            for i, j in locked:
                if ord(mlst[i][j])-65 == tk:
                    erase.append((i, j))
                    dq.append((i, j))
            for i, j in erase:
                locked.remove((i, j))
        
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<h and 0<=ny<w:
                if mlst[nx][ny] != '*' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx, ny))

    print(docs_cnt - len(docs))