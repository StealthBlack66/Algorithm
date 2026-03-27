from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

turns = deque()
L = int(input())
for _ in range(L):
    t, c = input().split()
    turns.append((int(t), c))

snake = deque([(0, 0)])
visited = {(0, 0)}
r, c = 0, 0
d = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0

while True:
    time += 1
    nr, nc = r + dx[d], c + dy[d]

    if not (0 <= nr < N and 0 <= nc < N) or (nr, nc) in visited:
        break

    if graph[nr][nc] == 0:      # 사과 없음 → 꼬리 제거
        tail = snake.pop()
        visited.remove(tail)
    else:
        graph[nr][nc] = 0       # 사과 먹기

    snake.appendleft((nr, nc))
    visited.add((nr, nc))
    r, c = nr, nc

    if turns and time == turns[0][0]:
        _, dir = turns.popleft()
        d = (d+1)%4 if dir == 'D' else (d+3)%4

print(time)