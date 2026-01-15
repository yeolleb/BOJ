# 2448
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
wide = 2*n - 1
t = [[" " for _ in range(wide)]for __ in range(n)]

def draw(i, j):
    t[i][j] = "*"
    t[i+1][j-1] = "*"
    t[i+1][j+1] = "*"
    t[i+2][j-2] = "*"
    t[i+2][j-1] = "*"
    t[i+2][j] = "*"
    t[i+2][j+1] = "*"
    t[i+2][j+2] = "*"

def search(row, col, height):
    while height > 3:
        size = height//2
        search(row+size, col-size, size)
        search(row+size, col+size, size)
        height = height//2

    if height == 3:
        return draw(row, col)

search(0, n-1, n)

# 구분자.join(문자열들의 리스트)
for i in t:
    print("".join(i))

# 일반 출력은 시간초과
# for i in range(n):
#     for j in range(wide):
#         print(t[i][j], end="")
#     print()