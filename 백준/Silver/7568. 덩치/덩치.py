N = int(input())

arr = []
for _ in range(N):
    w, h = map(int, input().split())
    arr.append((w, h))

for i in arr:
    rank = 1
    for j in arr:
        if (i[0] != j[0]) & (i[1] != j[1]):
            if (i[0] < j[0]) & (i[1] < j[1]):
                rank += 1

    print(rank, end=' ')
print()