# 13460
import sys
from collections import deque
input = sys.stdin.readline
 
n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(input().strip()))

red = (0, 0)
blue = (0, 0)
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'R':
            red = (i, j)
            lst[i][j] = '.'
        elif lst[i][j] == 'B':
            blue = (i, j)
            lst[i][j] = '.'

# 공 이동 시키기 (dir 위(0), 오(1), 아래(2), 왼(3))
def cal(rx, ry, bx, by, dir):
    isFail = False
    isRedRemoved = False
    isBlueFirst = True

    # 위(0)
    if dir == 0:
        # 순서
        if ry == by:
            if rx < bx:
                isBlueFirst = False
        if isBlueFirst:
            # 파랑
            while not isFail:
                if lst[bx][by] == 'O':
                    isFail = True
                    break
                elif lst[bx][by] != '.' or (bx == rx and by == ry):
                    bx += 1
                    break
                else:
                    bx -= 1
            # 빨강
            while not isFail:
                if lst[rx][ry] == 'O':
                    isRedRemoved = True
                    break
                elif lst[rx][ry] != '.' or (bx == rx and by == ry):
                    rx += 1
                    break
                else:
                    rx -= 1
        else:
            # 빨강
            while not isFail:
                if lst[rx][ry] == 'O':
                    isRedRemoved = True
                    break
                elif lst[rx][ry] != '.' or (bx == rx and by == ry):
                    rx += 1
                    break
                else:
                    rx -= 1
            # 파랑
            while not isFail:
                if lst[bx][by] == 'O':
                    isFail = True
                    break
                elif lst[bx][by] != '.' or (bx == rx and by == ry):
                    bx += 1
                    break
                else:
                    bx -= 1
    # 오(1)
    elif dir == 1:
        # 순서
        if rx == bx:
            if ry > by:
                isBlueFirst = False
        if isBlueFirst:
            # 파랑
            while not isFail:
                if lst[bx][by] == 'O':
                    isFail = True
                    break
                elif lst[bx][by] != '.' or (bx == rx and by == ry):
                    by -= 1
                    break
                else:
                    by += 1
            # 빨강
            while not isFail:
                if lst[rx][ry] == 'O':
                    isRedRemoved = True
                    break
                elif lst[rx][ry] != '.' or (bx == rx and by == ry):
                    ry -= 1
                    break
                else:
                    ry += 1
        else:
            # 빨강
            while not isFail:
                if lst[rx][ry] == 'O':
                    isRedRemoved = True
                    break
                elif lst[rx][ry] != '.' or (bx == rx and by == ry):
                    ry -= 1
                    break
                else:
                    ry += 1
            # 파랑
            while not isFail:
                if lst[bx][by] == 'O':
                    isFail = True
                    break
                elif lst[bx][by] != '.' or (bx == rx and by == ry):
                    by -= 1
                    break
                else:
                    by += 1
    # 아래(2)
    elif dir == 2:
        # 순서
        if ry == by:
            if rx > bx:
                isBlueFirst = False
        if isBlueFirst:
            # 파랑
            while not isFail:
                if lst[bx][by] == 'O':
                    isFail = True
                    break
                elif lst[bx][by] != '.' or (bx == rx and by == ry):
                    bx -= 1
                    break
                else:
                    bx += 1
            # 빨강
            while not isFail:
                if lst[rx][ry] == 'O':
                    isRedRemoved = True
                    break
                elif lst[rx][ry] != '.' or (bx == rx and by == ry):
                    rx -= 1
                    break
                else:
                    rx += 1
        else:
            # 빨강
            while not isFail:
                if lst[rx][ry] == 'O':
                    isRedRemoved = True
                    break
                elif lst[rx][ry] != '.' or (bx == rx and by == ry):
                    rx -= 1
                    break
                else:
                    rx += 1
            # 파랑
            while not isFail:
                if lst[bx][by] == 'O':
                    isFail = True
                    break
                elif lst[bx][by] != '.' or (bx == rx and by == ry):
                    bx -= 1
                    break
                else:
                    bx += 1
    # 왼(3)
    else:
        # 순서
        if rx == bx:
            if ry < by:
                isBlueFirst = False
        if isBlueFirst:
            # 파랑
            while not isFail:
                if lst[bx][by] == 'O':
                    isFail = True
                    break
                elif lst[bx][by] != '.' or (bx == rx and by == ry):
                    by += 1
                    break
                else:
                    by -= 1
            # 빨강
            while not isFail:
                if lst[rx][ry] == 'O':
                    isRedRemoved = True
                    break
                elif lst[rx][ry] != '.' or (bx == rx and by == ry):
                    ry += 1
                    break
                else:
                    ry -= 1
        else:
            # 빨강
            while not isFail:
                if lst[rx][ry] == 'O':
                    isRedRemoved = True
                    break
                elif lst[rx][ry] != '.' or (bx == rx and by == ry):
                    ry += 1
                    break
                else:
                    ry -= 1
            # 파랑
            while not isFail:
                if lst[bx][by] == 'O':
                    isFail = True
                    break
                elif lst[bx][by] != '.' or (bx == rx and by == ry):
                    by += 1
                    break
                else:
                    by -= 1
    return rx, ry, bx, by, isFail, isRedRemoved

dq = deque()
for r in range(4):
    dq.append((red[0], red[1], blue[0], blue[1], r, 1))

isImpossible = True
while dq:
    rx, ry, bx, by, dir, cnt = dq.popleft()
    redX, redY, blueX, blueY, isFail, isRedRemoved = cal(rx, ry, bx, by, dir)

    if isFail:
        continue
    elif isRedRemoved:
        print(cnt)
        isImpossible = False
        break
    elif cnt >= 10:
        continue

    for r in range(4):
        dq.append((redX, redY, blueX, blueY, r, cnt+1))

if isImpossible:
    print(-1)