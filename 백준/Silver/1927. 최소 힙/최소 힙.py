import heapq, sys

my_heap = []

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if not my_heap:
            print(0)
        else:
            print(heapq.heappop(my_heap))
    else:
        heapq.heappush(my_heap,x)