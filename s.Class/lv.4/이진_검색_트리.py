# 5639
# 참고: https://howudong.tistory.com/217
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

myList = []
while True:
    try:
        myList.append(int(input()))
    except:
        break

def LRV(s, e):
    if s > e:
        return
    
    root = myList[s]
    # 왼쪽 노드와 오른쪽 노드가 갈리는 인덱스
    temp = s+1

    while temp <= e:
        if root < myList[temp]:
            break
        temp += 1

    LRV(s+1, temp-1)
    LRV(temp, e)
    print(root)

LRV(0, len(myList)-1)