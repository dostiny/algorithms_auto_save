import math

def solution(n):
    answer = 2
    sqrt_num = math.sqrt(n)
    
    if float(int(sqrt_num)) == sqrt_num:
        answer = 1
    return answer