# 9527
# f(n): 0 ~ n까지의 1의 개수라 할때,
# f(2^k - 1) = k * 2^(k-1)
# 수학, 규칙찾기, 점화식?, 재귀
import sys
input = sys.stdin.readline

def cal_f(n):
    if n <= 0:
        return 0
    k = 0
    tmp = 1
    while tmp <= n:
        k += 1
        tmp *= 2
    k -= 1

    result = 0
    # k = 0일때는 res+1에서 추가됨
    if k > 0:
        result += k * (2 ** (k-1))
    res = n - 2 ** k

    result += res + 1
    result += cal_f(res)
    return result
    
a, b = map(int, input().split())

print(int(cal_f(b) - cal_f(a-1)))