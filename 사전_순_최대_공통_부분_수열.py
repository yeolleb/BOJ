# 30805
import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

common = set(list1)&set(list2)

answer = []
while common:
    max1 = max(common)
    answer.append(max1)
    
    idx1 = list1.index(max1)
    idx2 = list2.index(max1)
    
    list1 = list1[idx1+1:]
    list2 = list2[idx2+1:]
    
    common = set(list1)&set(list2)
    
print(len(answer))
print(*answer)