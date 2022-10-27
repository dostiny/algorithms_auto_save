N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
clean = 0
visited = [[0] * M for _ in range(N)]

visited[r][c] =1
clean += 1

while True:
    check = 0
    for _ in range(4):
        d = (d + 3) % 4
        nr, nc = r + dy[d], c + dx[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            clean += 1
            r, c = nr, nc
            check = 1
            break

    if check == 0:
        br, bc = r - dy[d], c - dx[d]
        if arr[br][bc] == 1:
            print(clean)
            break
        else:
            r, c = br, bc

