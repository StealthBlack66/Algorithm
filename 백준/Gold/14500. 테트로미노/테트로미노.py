import sys
input=sys.stdin.readline
from itertools import product

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 0

def dfs(r,c,depth,total):
    global result
    if depth == 4:
        result = max(result,total)
        return
    for i in range(4):
        nr,nc = r+dx[i], c+dy[i]
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr,nc,depth+1,total+arr[nr][nc])
            visited[nr][nc] = False

def T(r,c):
    total = arr[r][c]
    surroud = []
    for i in range(4):
        nr,nc = r+dx[i], c+dy[i]
        if 0<=nr<N and 0<=nc<M:
            total += arr[nr][nc]
            surroud.append(arr[nr][nc])
    if len(surroud) < 3:
        return 0
    
    if len(surroud) == 4:
        total -= min(surroud)

    return total

for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r,c,1,arr[r][c])
        visited[r][c] = False
        result = max(result,T(r,c))

print(result)