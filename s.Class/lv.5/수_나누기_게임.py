# 27172
# 내가 상대방을 나눠서 나머지 0이면 +1점
# 첫 풀이: 처음부터 순서대로 모든 숫자 비교 -> O(N^2)
# 정답: 수의 배수를 모두 찾아 점수 계산 -> O(NlogN)
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
xset = set(x)
score = [0]*1000001

for num in x:
    tmp = num * 2
    while tmp <= 1000000:
        if tmp in xset:
            score[num] += 1
            score[tmp] -= 1
        tmp += num

for num in x:
    print(score[num], end=" ")