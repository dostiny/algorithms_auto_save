def solution(n):
    answer = [n]
    num = n
    while num != 1:
        if num % 2:
            num = 3 * num + 1
        else :
            num = num // 2
        answer.append(num)
    return answer

print(solution(10))