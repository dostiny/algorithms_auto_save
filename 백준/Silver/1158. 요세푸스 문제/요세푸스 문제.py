import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
Q = deque()
for i in range(1, N + 1):
    Q.append(i)
ans = []
cnt = 0
while Q:
    cnt += 1
    a = Q.popleft()
    if cnt % K == 0:
        ans.append(str(a))
    else:
        Q.append(a)
result = ', '.join(ans)
print(f'<{result}>')