def solution(arr, queries):
    answer = arr
    for i in queries:
        a, b = i
        answer[a], answer[b] = answer[b], answer[a]
    return answer