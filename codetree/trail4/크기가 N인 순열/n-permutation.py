n = int(input())

def choose(lst):
    if len(lst) == n:
        print(*lst)
    
    for i in range(1, n+1):
        if i not in lst:
            lst.append(i)
            choose(lst)
            lst.pop()

plst = []
for i in range(1, n+1):
    plst.append(i)
    choose(plst)
    plst.pop()