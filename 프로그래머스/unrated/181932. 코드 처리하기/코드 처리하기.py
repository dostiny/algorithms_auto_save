def solution(code):
    answer = ''
    m = 0
    for i in range(len(code)):
        if m == 0:
            if code[i] == '1':
                m = 1
            elif i % 2 == 0:
                answer += code[i]
        else:
            if code[i] == '1':
                m = 0
            elif i % 2:
                answer += code[i]
    if answer == '':
        answer = "EMPTY"
    return answer