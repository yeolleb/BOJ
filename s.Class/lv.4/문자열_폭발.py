# 9935
# 참고: https://howudong.tistory.com/303
import sys
input = sys.stdin.readline
str = list(input().strip())
bomb = list(input().strip())

def cal():
    temp = []
    for _ in range(len(bomb)):
        temp.append(stack.pop())

    temp.reverse()
    if temp == bomb:
        return
    
    for i in temp:
        stack.append(i)

stack = []
for i in str:
    stack.append(i)
    
    if len(stack) >= len(bomb) and i == bomb[-1]:
        cal()

if len(stack) > 0:
    for i in range(len(stack)):
        print(stack[i], end="")
else:
    print("FRULA")



# s = 0
# while s <= len(str):
#     if s+len(bomb) <= len(str) and str[s] == bomb[0]:
#         isSame = True
#         for i in range(s, s+len(bomb)):
#             if str[i] != bomb[i-s]:
#                 isSame = False
#                 break
#         if isSame:
#             for _ in range(len(bomb)):
#                 str.pop(s)
#             s = 0
#         else:
#             s += 1
#     else:
#         s += 1

# if len(str) > 0:
#     for i in range(len(str)):
#         print(str[i], end="")
# else:
#     print("FRULA")