import sys
sys.setrecursionlimit(10000)

def dfs(x, y, visited, field):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and not visited[nx][ny] and field[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))

T = int(input())
results = []
    
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
        
    for _ in range(K):
         x, y = map(int, input().split())
         field[y][x] = 1
        
    worm_count = 0
        
    for i in range(N):
         for j in range(M):
              if field[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, visited, field)
                worm_count += 1
        
    results.append(worm_count)
    
for result in results:
    print(result)