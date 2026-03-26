import sys
input = sys.stdin.readline

N,M=map(int,input().split())
r,c,d = map(int,input().split())

arr = tuple(tuple(map(int,input().split())) for _ in range(N))
cleaned = [[0]*M for _ in range(N)]
answer = 0

idx = [-1,0,1,0]
idy = [0,1,0,-1]


while True:
    if cleaned[r][c] == 0:
        cleaned[r][c] = 1
        answer += 1
     
    found = False 
    for _ in range(4):
        d = (d+3)%4
        nx = r+idx[d]
        ny = c+idy[d]
        if arr[nx][ny] == 0 and cleaned[nx][ny] == 0:
            found = True
            r= nx 
            c= ny
            break

    if not found:
        back = (d+2)%4
        r = r+idx[back]
        c = c+idy[back]
        if arr[r][c] == 1:
            break


print(answer)