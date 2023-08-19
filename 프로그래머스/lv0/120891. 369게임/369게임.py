def solution(order):
    answer = 0
    for i in range(5, -1, -1):
        n = order // 10 ** i
        if n == 3 or n == 6 or n == 9:
            answer += 1
        order = order % 10 ** i
    return answer