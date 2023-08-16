def solution(n, k):
    answer = n * 12000 + k * 2000
    cnt = n // 10
    if cnt <= k:
        answer -= cnt * 2000
    return answer