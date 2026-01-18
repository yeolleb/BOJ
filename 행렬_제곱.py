# 10830
import sys
input = sys.stdin.readline

n, b = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]

def mul(U, V):
    n = len(U)
    z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            z[row][col] = e % 1000

    return z

def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    tmp = square(A, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

result = square(a, b)
for r in result:
    print(*r)