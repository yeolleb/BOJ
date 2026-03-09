# 7453
# pypy3
# append 리스트 생성방식은 시간이 오래 걸린다.
# -> 리스트 크기 미리 할당, 인덱스로 직접 채우기
import sys
input = sys.stdin.readline
n = int(input())

a = []
b = []
c = []
d = []

for _ in range(n):
    ta, tb, tc ,td = map(int, input().split())
    a.append(ta)
    b.append(tb)
    c.append(tc)
    d.append(td)

ab = [0]*(n*n)
cd = [0]*(n*n)

t = 0
for i in range(n):
    for j in range(n):
        ab[t] = a[i]+b[j]
        cd[t] = c[i]+d[j]
        t += 1

ab.sort()
cd.sort()

idx1 = 0
idx2 = n*n-1
ans = 0

while idx1 < n*n and idx2 > -1:
    plus = ab[idx1] + cd[idx2]

    if plus == 0:
        tmp_ab = ab[idx1]
        cnt1 = 0
        while idx1 < n*n and ab[idx1] == tmp_ab:
            cnt1 += 1
            idx1 += 1
        
        tmp_cd = cd[idx2]
        cnt2 = 0
        while idx2 > -1 and cd[idx2] == tmp_cd:
            cnt2 += 1
            idx2 -= 1
        
        ans += cnt1 * cnt2
        continue

    elif plus > 0:
        idx2 -= 1
    
    else:
        idx1 += 1

print(ans)