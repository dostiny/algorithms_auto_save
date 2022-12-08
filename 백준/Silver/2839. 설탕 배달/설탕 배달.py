N = int(input())
cnt = 0
result = 0

while N >= 0:
    if N % 5 == 0:
        cnt += (N // 5)
        result = cnt
        break
    N -= 3
    cnt += 1
else:
    result = -1

print(result)