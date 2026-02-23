# 11444
# 기존 dp -> 시간초과
# 벡터, 빠른 거듭제곱으로 풀이
# |F(n+1) F(n)|
# |F(n) F(n-1)|
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
matrix = [[1, 1], [1, 0]]

def square(a, b):
    tmp = [[0 for _ in range(2)]for _ in range(2)]

    # tmp[0][0] = a[0][0]*b[0][0] + a[0][1]*b[1][0]
    # tmp[0][1] = a[0][0]*b[0][1] + a[0][1]*b[1][1]
    # tmp[1][0] = a[1][0]*b[0][0] + a[1][1]*b[1][0]
    # tmp[1][1] = a[1][0]*b[0][1] + a[1][1]*b[1][1]

    for i in range(2):
        for j in range(2):
            for l in range(2):
                # 매 계산마다 mod. or 시간초과
                tmp[i][j] += a[i][l]*b[l][j] % 1000000007
    
    return tmp

def fibo(e):
    if e == 1:
        return matrix
    
    half = fibo(e // 2)
    
    if e % 2 == 0:
        return square(half, half)
    
    else:
        tmp  = square(matrix, half)
        return square(tmp, half)

print(fibo(n)[0][1] % 1000000007)