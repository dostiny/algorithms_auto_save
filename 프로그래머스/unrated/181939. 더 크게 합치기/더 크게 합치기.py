def solution(a, b):
    answer = 0
    n = m = 0
    if a > b:
        n = int(str(a) + str(b))
        m = int(str(b) + str(a))
    else:
        n = int(str(a) + str(b))
        m = int(str(b) + str(a))

    if n < m:
        answer = m
    else :
        answer = n
    return answer