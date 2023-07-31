def solution(a, b):
    answer = 0
    n = int(str(a) + str(b))
    m = 2 * a * b
    if n >= m:
        answer = n
    else :
        answer = m
    return answer
