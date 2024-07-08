import sys
from collections import deque

input = sys.stdin.readline
def find_min_time(N, build_times, rules, target):
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    time = [0] * (N + 1)
    
    for i in range(1, N + 1):
        time[i] = build_times[i-1]
    
    for X, Y in rules:
        graph[X].append(Y)
        indegree[Y] += 1
    
    queue = deque()
    dp = [0] * (N + 1)
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = time[i]
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            dp[neighbor] = max(dp[neighbor], dp[current] + time[neighbor])
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return dp[target]

T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    build_times = list(map(int, input().strip().split()))
    rules = [tuple(map(int, input().strip().split())) for _ in range(K)]
    target = int(input().strip())
    
    print(find_min_time(N, build_times, rules, target))