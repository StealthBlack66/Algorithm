import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
result = 0

dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            continue
        #가로
        if dp[i][j][0]:
            # -
            if j+1<N and arr[i][j+1] == 0:
                dp[i][j+1][0] += dp[i][j][0]
            # \
            if i+1<N and j+1<N and arr[i][j+1] == 0 and arr[i+1][j] == 0 and arr[i+1][j+1] == 0:
                dp[i+1][j+1][2] += dp[i][j][0]
        #세로
        if dp[i][j][1]:
            # \
            if i+1<N and j+1<N and arr[i][j+1] == 0 and arr[i+1][j] == 0 and arr[i+1][j+1] == 0:
                dp[i+1][j+1][2] += dp[i][j][1]
            # |
            if i+1<N and arr[i+1][j] == 0:
                dp[i+1][j][1] += dp[i][j][1]
        #대각선
        if dp[i][j][2]:
            # -
            if j+1<N and arr[i][j+1] == 0:
                dp[i][j+1][0] += dp[i][j][2]
            # \
            if i+1<N and j+1<N and arr[i][j+1] == 0 and arr[i+1][j] == 0 and arr[i+1][j+1] == 0:
                dp[i+1][j+1][2] += dp[i][j][2]
            # |
            if i+1<N and arr[i+1][j] == 0:
                dp[i+1][j][1] += dp[i][j][2]

for item in dp[N-1][N-1]:
    result += item

print(result)