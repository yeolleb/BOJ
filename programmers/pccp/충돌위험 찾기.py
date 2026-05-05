# 충돌위험 찾기
def solution(points, routes):
    pn = len(points)
    rn = len(routes)
            
    # 로봇별 초당 위치 
    time_positions = [[]for _ in range(rn)]
    
    for robot_idx in range(rn):
        for now_idx in range(len(routes[robot_idx])-1):
            nxt_idx = now_idx+1
            # points 인덱스 0부터 시작하므로 -1 하기
            now_point = routes[robot_idx][now_idx]-1
            nxt_point = routes[robot_idx][nxt_idx]-1
            
            x = points[now_point][0]
            y = points[now_point][1]
            nx = points[nxt_point][0]
            ny = points[nxt_point][1]
            
            # 행 맞추기
            while x != nx:
                time_positions[robot_idx].append((x, y))
                if x < nx:
                    x += 1
                elif x > nx:
                    x -= 1
            # 열 맞추기
            while y != ny:
                time_positions[robot_idx].append((x, y))
                if y < ny:
                    y += 1
                elif y > ny:
                    y -= 1
        # 도착
        time_positions[robot_idx].append((x, y))
    
    max_time = 0
    for i in range(rn):
        max_time = max(max_time, len(time_positions[i]))

    ans = 0
    for t in range(max_time):
        path = [[0 for _ in range(101)]for __ in range(101)]
        for i in range(rn):
            if len(time_positions[i]) <= t:
                continue
            r = time_positions[i][t][0]
            c = time_positions[i][t][1]
            if path[r][c] == 1:
                path[r][c] += 1
                ans += 1
            elif path[r][c] == 0:
                path[r][c] += 1
                
    return ans