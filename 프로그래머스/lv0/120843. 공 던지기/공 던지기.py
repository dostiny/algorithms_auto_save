def solution(numbers, k):
    answer = 0
    n = 1
    while n != k:
        numbers = numbers[2:] + numbers[:2]
        n += 1
        answer = numbers[0]
    return answer