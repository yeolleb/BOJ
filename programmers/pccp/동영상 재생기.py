# 동영상 재생기
# f-string(포맷 문자열), 형식 지정자
def solution(video_len, pos, op_start, op_end, commands):
    start_seconds = toSeconds(op_start)
    end_seconds = toSeconds(op_end)
    video_seconds = toSeconds(video_len)
    
    now = toSeconds(pos)
    
    if start_seconds <= now < end_seconds:
            now = end_seconds
    
    for comm in commands:
        if comm == "next":
            now += 10
            if now > video_seconds:
                now = video_seconds
                
        elif comm == "prev":
            now -= 10
            if now < 0:
                now = 0
        if start_seconds <= now < end_seconds:
            now = end_seconds
    
    m = now // 60
    s = now % 60
    
    return f"{m:02d}:{s:02d}"
    
def toSeconds(time):
    m, s = map(int, time.split(':'))
    return m*60 + s