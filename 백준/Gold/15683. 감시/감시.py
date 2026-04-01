import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

directions = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[3,0]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]]
}

camera = []
for r in range(N):
    for c in range(M):
        if 0 < arr[r][c] < 6:
            camera.append((r,c,arr[r][c]))

result = 64

def watch(board, r, c, d):
    for dir in d:
        nr, nc = r+dx[dir], c+dy[dir]
        while 0<=nr<N and 0<=nc<M:
            if board[nr][nc] == 6:
                break
            if board[nr][nc] == 0:
                board[nr][nc] = '#'
            nr += dx[dir]
            nc += dy[dir]

def dfs(idx, board):
    global result
    
    if idx == len(camera):
        cnt = sum(row.count(0) for row in board)
        result = min(result, cnt)
        return
    
    r,c,type = camera[idx]
    
    for d in directions[type]:
        new_board = [row[:] for row in board]
        watch(new_board, r, c, d)
        dfs(idx+1, new_board)

dfs(0, arr)
print(result)