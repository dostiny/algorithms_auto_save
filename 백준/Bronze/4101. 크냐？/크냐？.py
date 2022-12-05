numli = []
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    else:
        numli.append((N, M))
for N, M in numli:
    if N > M:
        print("Yes")
    else:
        print("No")