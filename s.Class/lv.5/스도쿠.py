# 2239
# 유사문제: 텀 프로젝트(9466)
# 재귀는 언제나 어렵다.. 종료조건 depth 이용하기 !!!!
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

lst = []
for _ in range(9):
    lst.append(list(map(int, input().strip())))

bk = []
for i in range(9):
    for j in range(9):
        if lst[i][j] == 0:
            bk.append((i, j))

# 가로
row_set = []
for i in range(9):
    tmp = set()
    for j in range(9):
        if lst[i][j] > 0:
            tmp.add(lst[i][j])
    row_set.append(tmp)

# 세로
col_set = []
for j in range(9):
    tmp = set()
    for i in range(9):
        if lst[i][j] > 0:
            tmp.add(lst[i][j])
    col_set.append(tmp)

# 박스
box_set = []
for row in 0, 3, 6:
    for col in 0, 3, 6:
        tmp = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                if lst[i][j] > 0:
                    tmp.add(lst[i][j])
        box_set.append(tmp)

def dfs(depth):
    if depth == len(bk):
        return True
    
    r, c = bk[depth]
    box_idx = (r//3)*3 + c//3

    for num in range(1, 10):
        if num not in row_set[r] and num not in col_set[c] and num not in box_set[box_idx]:
            lst[r][c] = num
            row_set[r].add(num)
            col_set[c].add(num)
            box_set[box_idx].add(num)

            if dfs(depth+1):
                return True
            else:
                row_set[r].remove(num)
                col_set[c].remove(num)
                box_set[box_idx].remove(num)
    return False

dfs(0)

for i in range(9):
    for j in range(9):
        print(lst[i][j], end="")
    print()