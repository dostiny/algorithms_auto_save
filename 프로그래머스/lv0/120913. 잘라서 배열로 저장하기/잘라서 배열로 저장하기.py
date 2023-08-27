def solution(my_str, n):
    answer = []
    cnt = 0
    st = ''
    for i in my_str:
        if cnt == n:
            answer.append(st)
            st = i
            cnt = 1
        else:
            st += i
            cnt += 1
    answer.append(st)
    return answer