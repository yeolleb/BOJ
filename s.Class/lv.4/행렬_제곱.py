# 10830
import sys
input = sys.stdin.readline

n, b = map(int, input().split())
myList = []

for i in range(n):
    myList.append(list(map(int, input().split())))

def cal(one, two):
    global n
    temp = [[0 for _ in range(n)]for __ in range(n)]
    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(n):
                t += (one[i][k] * two[k][j]) % 1000
            temp[i][j] = t
    return temp

def pow(e):
    if e == 1:
        return myList
    half = pow(e // 2)
    if e % 2 == 0:
        return cal(half, half)
    else:
        temp = cal(half, half)
        return cal(temp, myList)

ans = pow(b)

for i in range(n):
    for j in range(n):
        print(ans[i][j] % 1000, end=" ")
    print()  