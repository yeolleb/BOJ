# 14888
# dfs를 생각했으나 op 리스트에 대한 문제를 딥카피를 이용하여 풀었다.
# 이는 매우 무겁기 때문에 백트래킹을 이용하는게 훨씬 낫다.......... 왜 복구하면 된다는걸 생각 못했을까 ...........
import sys, copy
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
# +, -, *, /
op = list(map(int, input().split()))

maxans = -sys.maxsize
minans = sys.maxsize

q = []

for i in range(4):
    if op[i] > 0:
        if i == 0:
            res = a[0] + a[1]
        elif i == 1:
            res = a[0] - a[1]
        elif i == 2:
            res = a[0] * a[1]
        elif i == 3:
            res = int(a[0] / a[1])
        lst = copy.deepcopy(op)
        lst[i] -= 1
        q.append((res, 2, lst))

while q:
    res, idx, cmd = q.pop()

    if idx == n:
        maxans = max(maxans, res)
        minans = min(minans, res)

    for i in range(4):
        if cmd[i] > 0:
            if i == 0:
                tmp = res + a[idx]
            elif i == 1:
                tmp = res - a[idx]
            elif i == 2:
                tmp = res * a[idx]
            elif i == 3:
                tmp = int(res / a[idx])
            lst = copy.deepcopy(cmd)
            lst[i] -= 1
            q.append((tmp, idx+1, lst))

print(maxans)
print(minans)