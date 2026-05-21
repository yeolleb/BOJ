# 석유 시추
from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])

    # 석유 정보
    oil_dict = {}
    group_lst = [[0 for _ in range(m)]for __ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False for _ in range(m)]for __ in range(n)]
    dq = deque()
    now_group_num = 0
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                now_group_num += 1
                visited[i][j] = True
                dq.append((i, j))
                cnt = 1
                group_lst[i][j] = now_group_num
                
                while dq:
                    x, y = dq.popleft()
                    
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0<=nx<n and 0<=ny<m and land[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            dq.append((nx, ny))
                            cnt += 1
                            group_lst[nx][ny] = now_group_num
                oil_dict[now_group_num] = cnt
                
    ans = [0]*m
    for j in range(m):
        g_set = set()
        for i in range(n):
            if group_lst[i][j] > 0 and group_lst[i][j] not in g_set:
                g_set.add(group_lst[i][j])
                ans[j] += oil_dict[group_lst[i][j]]
    return max(ans)