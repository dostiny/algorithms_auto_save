def solution(numLog):
    answer = ''
    for i in range(len(numLog)):
        if i == 0:
            continue
        n = numLog[i] - numLog[i-1]
        if n == 1:
            answer += 'w'
        elif n == -1:
            answer += 's'
        elif n == 10:
            answer += 'd'
        elif n == -10:
            answer += 'a'
    return answer