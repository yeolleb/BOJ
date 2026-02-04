# 9019
# https://jominseoo.tistory.com/93
# 문자열은 시간초과 발생
# bfs 시간초과에 반드시 방문 체크
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

def bfs(a, b):
    dq = deque()
    visited.add(a)
    dq.append((a, ""))

    while dq:
        n, cmd = dq.popleft()

        if n == b:
            break
        
        for op in ['D', 'S', 'L', 'R'] :
            if op == 'D':
                temp = 2 * n % 10000
            
            if op == 'S':
                temp = (n-1) % 10000
            
            if op == 'L':
                temp = n//1000 + (n%1000)*10

            if op == 'R':
                temp = n//10 + (n%10)*1000
            
            if temp not in visited:
                visited.add(temp)
                dq.append((temp, cmd+op))

    return cmd

for _ in range(t):
    a, b = map(int, input().split())
    visited = set()

    print(bfs(a, b))