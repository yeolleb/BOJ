# 2143
import sys
input = sys.stdin.readline

t = int(input())

a = int(input())
alst = list(map(int, input().split()))

asum = []
for i in range(a):
    tasum = alst[i]
    asum.append(tasum)
    for j in range(i+1, a):
        tasum += alst[j]
        asum.append(tasum)

b = int(input())
blst = list(map(int, input().split()))
bsum = []
for i in range(b):
    tbsum = blst[i]
    bsum.append(tbsum)
    for j in range(i+1, b):
        tbsum += blst[j]
        bsum.append(tbsum)

asum.sort()
bsum.sort()

ans = 0
aidx = 0
bidx = len(bsum) - 1

while aidx < len(asum) and bidx > -1:
    temp = asum[aidx] + bsum[bidx]

    if temp == t:
        acnt = 0
        atmp = asum[aidx]
        while aidx < len(asum):
            if asum[aidx] == atmp:
                acnt += 1
                aidx += 1
            else:
                break
        bcnt = 0
        btmp = bsum[bidx]
        while bidx > -1:
            if bsum[bidx] == btmp:
                bcnt += 1
                bidx -= 1
            else:
                break
        ans += acnt * bcnt
    elif temp < t:
        aidx += 1
    else:
        bidx -= 1

print(ans)