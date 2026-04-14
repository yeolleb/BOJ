# 14889
import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    s.append(list(map(int, input().split())))

def cal_score(team):
    res = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            res += s[team[i]][team[j]]
            res += s[team[j]][team[i]]
    return res

# start로 중복 제거
def dfs(depth, start):
    global ans

    if depth == n//2:
        teamA = []
        teamB = []
        for i in range(n):
            if visited[i]:
                teamA.append(i)
            else:
                teamB.append(i)

        scoreA = cal_score(teamA)
        scoreB = cal_score(teamB)
        ans = min(ans, abs(scoreA - scoreB))
        return
    
    for i in range(start, n):
        visited[i] = True
        dfs(depth+1, i+1)
        visited[i] = False

visited = [False]*n
ans = sys.maxsize

dfs(0, 0)

print(ans)