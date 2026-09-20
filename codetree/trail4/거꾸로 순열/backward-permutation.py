n = int(input())

visited = [False]*(n+1)

def choose(lst):
    if len(lst) >= n:
        print(*lst)
        return  
    
    for i in range(n, 0, -1):
        if not visited[i]:
            visited[i] = True
            lst.append(i)
            
            choose(lst)

            visited[i] = False
            lst.pop()

plst = []
choose(plst)