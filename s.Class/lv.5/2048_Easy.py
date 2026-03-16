# 12100
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

# 방향에 따라 합치기
# 위(0), 오(1), 아래(2), 왼(3)
def cal(temp_lst, dir):
    tmp = [[0 for _ in range(n)]for __ in range(n)]
    if dir == 0:
        for j in range(n):
            i = 0
            while i < n:
                if temp_lst[i][j] == 0:
                    i += 1
                else:
                    nxti = i+1
                    while 0 <= nxti < n:
                        if temp_lst[nxti][j] != 0:
                            break
                        else:
                            nxti += 1
                    if 0 <= nxti < n and temp_lst[nxti][j] != 0:
                        if temp_lst[i][j] == temp_lst[nxti][j]:
                            tmp_i = i
                            while 0 <= tmp_i < n:
                                if tmp[tmp_i][j] == 0:
                                    tmp_i -= 1
                                else:
                                    break
                            tmp_i += 1
                            tmp[tmp_i][j] = temp_lst[i][j] + temp_lst[nxti][j]
                            i = nxti + 1
                        else:
                            tmp_i = i
                            while 0 <= tmp_i < n:
                                if tmp[tmp_i][j] == 0:
                                    tmp_i -= 1
                                else:
                                    break
                            tmp_i += 1
                            tmp[tmp_i][j] = temp_lst[i][j]
                            i = nxti
                    else:
                        tmp_i = i
                        while 0 <= tmp_i < n:
                            if tmp[tmp_i][j] == 0:
                                tmp_i -= 1
                            else:
                                break
                        tmp_i += 1
                        tmp[tmp_i][j] = temp_lst[i][j]
                        i += 1
    elif dir == 1:
        for i in range(n):
            j = n-1
            while j > -1:
                if temp_lst[i][j] == 0:
                    j -= 1
                else:
                    nxtj = j-1
                    while 0 <= nxtj < n:
                        if temp_lst[i][nxtj] != 0:
                            break
                        else:
                            nxtj -= 1
                    if 0 <= nxtj < n and temp_lst[i][nxtj] != 0:
                        if temp_lst[i][j] == temp_lst[i][nxtj]:
                            tmp_j = j
                            while 0 <= tmp_j < n:
                                if tmp[i][tmp_j] == 0:
                                    tmp_j += 1
                                else:
                                    break
                            tmp_j -= 1
                            tmp[i][tmp_j] = temp_lst[i][j] + temp_lst[i][nxtj]
                            j = nxtj - 1
                        else:
                            tmp_j = j
                            while 0 <= tmp_j < n:
                                if tmp[i][tmp_j] == 0:
                                    tmp_j += 1
                                else:
                                    break
                            tmp_j -= 1
                            tmp[i][tmp_j] = temp_lst[i][j]
                            j = nxtj
                    else:
                        tmp_j = j
                        while 0 <= tmp_j < n:
                            if tmp[i][tmp_j] == 0:
                                tmp_j += 1
                            else:
                                break
                        tmp_j -= 1
                        tmp[i][tmp_j] = temp_lst[i][j]
                        j -= 1
    elif dir == 2:
        for j in range(n):
            i = n-1
            while i > -1:
                if temp_lst[i][j] == 0:
                    i -= 1
                else:
                    nxti = i-1
                    while 0 <= nxti < n:
                        if temp_lst[nxti][j] != 0:
                            break
                        else:
                            nxti -= 1
                    if 0 <= nxti < n and temp_lst[nxti][j] != 0:
                        if temp_lst[i][j] == temp_lst[nxti][j]:
                            tmp_i = i
                            while 0 <= tmp_i < n:
                                if tmp[tmp_i][j] == 0:
                                    tmp_i += 1
                                else:
                                    break
                            tmp_i -= 1
                            tmp[tmp_i][j] = temp_lst[i][j] + temp_lst[nxti][j]
                            i = nxti - 1
                        else:
                            tmp_i = i
                            while 0 <= tmp_i < n:
                                if tmp[tmp_i][j] == 0:
                                    tmp_i += 1
                                else:
                                    break
                            tmp_i -= 1
                            tmp[tmp_i][j] = temp_lst[i][j]
                            i = nxti
                    else:
                        tmp_i = i
                        while 0 <= tmp_i < n:
                            if tmp[tmp_i][j] == 0:
                                tmp_i += 1
                            else:
                                break
                        tmp_i -= 1
                        tmp[tmp_i][j] = temp_lst[i][j]
                        i -= 1
    else:
        for i in range(n):
            j = 0
            while j < n:
                if temp_lst[i][j] == 0:
                    j += 1
                else:
                    nxtj = j+1
                    while 0 <= nxtj < n:
                        if temp_lst[i][nxtj] != 0:
                            break
                        else:
                            nxtj += 1
                    if 0 <= nxtj < n and temp_lst[i][nxtj] != 0:
                        if temp_lst[i][j] == temp_lst[i][nxtj]:
                            tmp_j = j
                            while 0 <= tmp_j < n:
                                if tmp[i][tmp_j] == 0:
                                    tmp_j -= 1
                                else:
                                    break
                            tmp_j += 1
                            tmp[i][tmp_j] = temp_lst[i][j] + temp_lst[i][nxtj]
                            j = nxtj + 1
                        else:
                            tmp_j = j
                            while 0 <= tmp_j < n:
                                if tmp[i][tmp_j] == 0:
                                    tmp_j -= 1
                                else:
                                    break
                            tmp_j += 1
                            tmp[i][tmp_j] = temp_lst[i][j]
                            j = nxtj
                    else:
                        tmp_j = j
                        while 0 <= tmp_j < n:
                            if tmp[i][tmp_j] == 0:
                                tmp_j -= 1
                            else:
                                break
                        tmp_j += 1
                        tmp[i][tmp_j] = temp_lst[i][j]
                        j += 1
    return tmp

# 최댓값 구하기
def find_max(tmp_lst):
    tmp = 0
    for i in range(n):
        tmp = max(tmp, max(tmp_lst[i]))
    return tmp

dq = deque()
for r in range(4):
    dq.append((lst, r, 1))

ans = 0
while dq:
    tmp_lst, dir, cnt = dq.popleft()
    result_lst = cal(tmp_lst, dir)
    ans = max(ans, find_max(result_lst))

    if cnt < 5:
        for r in range(4):
            dq.append((result_lst, r, cnt+1))

print(ans)