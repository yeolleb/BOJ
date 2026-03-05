# 1202
# 원래 가방 하나당 보석을 다 탐색해야된다. O(N^2)
# 보석을 한번씩만 탐색하기 위해서 **투포인터** 이용
# 구현 방식은 엄청 간단하고 나도 거의 다 풀었는데 시간 복잡도를 잡을 투포인터만 생각해내자
import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewlst = []

for _ in range(n):
    m, v = map(int, input().split())
    jewlst.append((m, v))

packlst = []
for _ in range(k):
    c = int(input())
    packlst.append(c)

# 정렬하고 순서대로 비교하면 최대값이다.
jewlst.sort()
packlst.sort()

ans = 0
idx = 0
hq = []
for p in packlst:
    # 무게가 작은 보석들 max heap에 저장
    while idx < n and jewlst[idx][0] <= p:
        m, v = jewlst[idx]
        heapq.heappush(hq, (-v, m))
        idx += 1

    if not hq:
        continue

    # 최대값 보석 pop
    # 그때 그때 최적의 해 도출 (greedy)
    minusV, m = heapq.heappop(hq)
    v = -minusV
    ans += v

print(ans)