def min_jumps(x, y):
    distance = y - x
    max_jump = 1
    total_distance = 0
    jumps = 0

    while total_distance < distance:
        jumps += 1
        total_distance += max_jump
        if jumps % 2 == 0:
            max_jump += 1
    return jumps

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    print(min_jumps(x, y))