while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    elif N > M:
        print('Yes')
    else:
        print('No')