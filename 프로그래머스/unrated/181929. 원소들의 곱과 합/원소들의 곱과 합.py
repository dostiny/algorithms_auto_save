def solution(num_list):
    answer = 0
    mul, squ = 1, 0
    for i in num_list:
        mul *= i
        squ += i
    squ = squ**2
    if mul < squ:
        answer = 1
    return answer