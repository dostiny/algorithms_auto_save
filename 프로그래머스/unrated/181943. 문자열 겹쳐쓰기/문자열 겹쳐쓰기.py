def solution(my_string, overwrite_string, s):
    answer = ''
    n = len(overwrite_string)
    m, j = 0, 0
    for i in range(len(my_string)):
        if i == s:
            m = 1

        if m == 0:
            answer += my_string[i]
        elif m == 1:
            answer += overwrite_string[j]
            j += 1
            if j == n:
                m = 0
    return answer

