import math

def find_intersection_count(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if d == 0 and r1 == r2:
        return -1
    if d > r1 + r2 or d < abs(r1 - r2):
        return 0
    if d == r1 + r2 or d == abs(r1 - r2):
        return 1
    return 2

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(find_intersection_count(x1, y1, r1, x2, y2, r2))