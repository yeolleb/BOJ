# 붕대 감기
import sys
input = sys.stdin.readline

def solution(bandage, health, attacks):
    at_dict = {}
    for t, d in attacks:
        at_dict[t] = d
    max_health = health
    now = 0
    seq = 0
    while now < attacks[-1][0]:
        now += 1
        # print("--------------------now is ", now)
        
        if now in at_dict:
            health -= at_dict[now]
            seq = 0
            if health <= 0:
                return -1
        else:
            health += bandage[1]
            seq += 1
            if seq >= bandage[0]:
                health += bandage[2]
                seq = 0
            if health > max_health:
                health = max_health
        # print(health)
    return health