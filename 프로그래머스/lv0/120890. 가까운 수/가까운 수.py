def solution(array, n):
    answer = 0
    minnum = 100
    for i in array:
        dif = n - i
        if 0 > dif:
            dif = -dif
        if minnum > dif:
            minnum = dif
            answer = i
        elif minnum == dif:
            answer = min(answer, i)
    return answer