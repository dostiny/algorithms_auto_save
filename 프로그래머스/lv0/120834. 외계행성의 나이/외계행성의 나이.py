def solution(age):
    alpha = list('abcdefghij')
    answer = ''
    for i in range(3, -1, -1):
        pro = age // 10 ** i
        age = age % 10 ** i
        if answer == '' and pro == 0:
            continue
        answer += alpha[pro]
    return answer