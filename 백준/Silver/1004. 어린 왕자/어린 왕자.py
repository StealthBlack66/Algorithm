import math

def is_inside(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 < r ** 2

def count_intersections(x1, y1, x2, y2, planets):
    count = 0
    for cx, cy, r in planets:
        start_inside = is_inside(x1, y1, cx, cy, r)
        end_inside = is_inside(x2, y2, cx, cy, r)
        if start_inside != end_inside:
            count += 1
    return count

T = int(input())
results = []

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = []
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        planets.append((cx, cy, r))
    results.append(count_intersections(x1, y1, x2, y2, planets))

for result in results:
    print(result)
