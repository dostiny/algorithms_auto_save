def solution(emergency):
    answer = []
    num_li = []
    for i in emergency:
        if num_li == []:
            num_li.append(i)
            answer.append(1)
        else:
            n = 1
            for j in range(len(num_li)):
                if num_li[j] < i:
                    answer[j] += 1
                else:
                    n += 1
            num_li.append(i)
            answer.append(n)

    return answer