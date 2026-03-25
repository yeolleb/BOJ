# 9527
def count(num):  
    cnt = 0  
    bin_num = bin(num)[2:]  
    length = len(bin_num)  
    for i in range(length):  
        if bin_num[i] == '1':  
            # num보다 크지 않으면서 가장 큰 2의 거듭제곱 수  
            val = length-i-1  
            cnt += one_sum[val]  
            # 가장 앞자리 1 개수를 추가로 더해주기  
            cnt += (num - 2**val + 1)  
            num = num - 2 ** val  
    return cnt  

x, y = map(int, input().split())  
one_sum = [0 for _ in range(60)]  

for i in range(1, 60):  
    one_sum[i] = 2**(i-1) + 2 * one_sum[i-1]  

print(count(y) - count(x-1))