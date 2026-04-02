import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 초기 위치
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark = (i, j)
            arr[i][j] = 0

size = 2
eat_cnt = 0
time = 0

def bfs(sr, sc):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 0

    fishes = []

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dx[d], c + dy[d]

            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == -1 and arr[nr][nc] <= size:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

                    if 0 < arr[nr][nc] < size:
                        fishes.append((visited[nr][nc], nr, nc))

    return sorted(fishes)

while True:
    result = bfs(shark[0], shark[1])

    if not result:
        break

    dist, r, c = result[0]

    time += dist
    shark = (r, c)

    arr[r][c] = 0
    eat_cnt += 1

    if eat_cnt == size:
        size += 1
        eat_cnt = 0

print(time)