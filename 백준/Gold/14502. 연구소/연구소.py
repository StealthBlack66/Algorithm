import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
# 바이러스 확산
def bfs(arr):
    queue = deque()
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 2:
                queue.append((r,c))

    while queue:
        r,c = queue.popleft()
        for idx in range(4):
            nr,nc = r+dx[idx], c+dy[idx]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                queue.append((nr,nc))
    return arr

# 값이 0인 영역 구하기
cleanArea = []
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            cleanArea.append((r,c))

# 조합별 0인 영역 개수 구하기
result=0  #0 개수의 최댓값
for area in combinations(cleanArea,3):
    num=0     #현재 0 개수
    testArea = copy.deepcopy(arr)
    for r,c in area:
        testArea[r][c] = 1
    testArea = bfs(testArea)
    #print(testArea)     #디버깅
    for i in range(N):
        num += testArea[i].count(0)
    result = max(result,num)

print(result)
