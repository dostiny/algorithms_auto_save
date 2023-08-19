def solution(array):
    maxNum = 0
    idx = 0
    for i in range(len(array)):
        if array[i] > maxNum:
            maxNum = array[i]
            idx = i
    answer = [maxNum, idx]
    return answer