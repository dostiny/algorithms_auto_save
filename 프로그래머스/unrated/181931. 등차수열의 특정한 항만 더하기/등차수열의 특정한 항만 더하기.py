def solution(a, d, included):
    answer = 0
    n = a
    for i in range(len(included)):
        if i == 0 and included[i]:
            answer += a
        elif included[i]:
            answer += n
        n += d
    return answer