# 수식 복원하기
# 2~9진법 중 하나
# int(string, N): N진법을 10진법으로 변환
def solution(expressions):
    hints = []
    quests = []
    
    en = len(expressions)
    for i in range(en):
        lst = expressions[i].split(' ')
        if lst[4] == 'X':
            quests.append(lst)
        else:
            hints.append(lst)
            
    # 최소 진법 구하기
    max_num = 0
    for h in hints:
        for k in 0,2,4:
            for c in list(h[k]):
                max_num = max(max_num, int(c))
    for q in quests:
        for k in 0,2:
            for c in list(q[k]):
                max_num = max(max_num, int(c))
            
    temp = ['']*en
    for n in range(max_num+1, 10):
        isChecked = True
        for i in range(len(hints)):
            l = int(hints[i][0], n)
            r = int(hints[i][2], n)
            
            if hints[i][1] == '+':
                res = l+r
            else:
                res = l-r
            
            if res != int(hints[i][4], n):
                isChecked = False
                break
                
        if not isChecked:
            continue
        
        for i in range(len(quests)):
            l = int(quests[i][0], n)
            r = int(quests[i][2], n)
            
            if quests[i][1] == '+':
                res_10 = l+r
            else:
                res_10 = l-r
            
            if res_10 == 0:
                res_str = '0'
            else:
                res_str = ''
                while res_10:
                    res_str = str(res_10%n)+res_str
                    res_10 //= n
            
            if quests[i][4] == 'X':
                quests[i][4] = res_str
            else:
                if res_str != quests[i][4]:
                    quests[i][4] = '?'
    ans = []
    for q in quests:
        # ans.append(" ".join(q))
        ans.append(q[0]+' '+q[1]+' '+q[2]+' '+q[3]+' '+q[4])
    return ans