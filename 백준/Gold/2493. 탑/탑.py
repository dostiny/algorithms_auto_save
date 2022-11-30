import sys;

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0 for i in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])

print(*answer)