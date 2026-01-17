# 11054
import sys
input = sys.stdin.readline

n = int(input())
myList = list(map(int, input().split()))

# 증가하는 수열
dpU = [0]*n
for i in range(n):
    temp = 0
    for j in range(i+1):
        if myList[j] < myList[i]:
            temp = max(temp, dpU[j])
    dpU[i] = temp + 1

# 감소하는 수열
dpD = [0]*n
for i in range(n-1, -1, -1):
    temp = 0
    for j in range(n-1, i-1, -1):
        if myList[j] < myList[i]:
            temp = max(temp, dpD[j])
    dpD[j] = temp + 1

ans = 0
for i in range(n):
    ans = max(ans, dpU[i] + dpD[i] - 1)

print(ans)


# def cal(s):
#     # 감소하는 수열
#     dpD = [0]*n
#     for i in range(s+1, n):
#         if myList[s] <= myList[i]:
#             continue
#         temp = 0
#         for j in range(s+1, i+1):
#             if myList[j] > myList[i]:
#                 temp = max(temp, dpD[j])
#         dpD[j] = temp + 1
#     return max(dpD)

# # ans[i]: myList[i]가 가장 클때의 가장 긴 바이토닉 수열 길이
# ans = [0]*n

# # 증가하는 수열
# dpU = [0]*n
# for i in range(n):
#     temp = 0
#     for j in range(i+1):
#         if myList[j] < myList[i]:
#             temp = max(temp, dpU[j])
#     dpU[i] = temp + 1
#     ans[i] = dpU[i] + cal(i)

# print(max(ans))