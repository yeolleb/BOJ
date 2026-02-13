# 1918
# 후위 표기식
# 알파벳은 바로 출력
# 연산자는 스택에 쌓다가 이전 연산자 보다 우선순위가 높거나 같으면 모두 출력
# *나 /가 들어왔을 때는 동급인 *나 /일 때만 반복해서 출력
# ) 가 나오면 ( 나올때 까지 모두 출력
import sys
input = sys.stdin.readline
lst = list(input().strip())

stack = []
ans = ''

for str in lst:
    # 알파벳은 바로 출력
    if str.isalpha():
        ans += str
    else:
        if str == '(':
            stack.append(str)
        # ( 나올때 까지 모두 출력
        elif str == ')':
            while stack:
                tmp = stack.pop()
                if tmp == '(':
                    break
                ans += tmp
        # 이전 연산자 보다 우선순위가 높거나 같으면 모두 출력 -> ( 직전까지 !
        elif str == '+' or str == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(str)
        elif str == '*' or str == '/':
            while stack and stack[-1] != '(' and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(str)

while stack:
    ans += stack.pop()

print(ans)