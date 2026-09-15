# xor 연산자: ^

n, m = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

def dfs(lst, idx):
    global ans

    if len(lst) == m:
        temp = 0
        for i in lst:
            temp = temp ^ i
        ans = max(ans, temp)
        return
    
    for i in range(idx+1, n):
        lst.append(A[i])
        dfs(lst, i)
        lst.pop()

plst = []
dfs(plst, -1)

print(ans)