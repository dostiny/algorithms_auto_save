def solution(arr, queries):
    answer = []
    for ar in queries:
        s, e, k = ar
        i = 1000000
        for j in arr[s:e+1]:
            if j > k and i > j:
                i = j
        if i == 1000000:
            answer.append(-1)
        else:
            answer.append(i)
    return answer