# 퍼즐 게임 챌린지
def solution(diffs, times, limit):
    n = len(diffs)

    # binary search
    l = 1
    r = max(diffs)
    
    while l < r:
        res = 0
        mid = (l+r) // 2
        
        # calculate times
        for i in range(n):
            if diffs[i] <= mid:
                res += times[i]
            else:
                res += (times[i] + times[i-1]) * (diffs[i] - mid) + times[i]
                
        if res <= limit:
            r = mid
        else:
            l = mid + 1
    return l