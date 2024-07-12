import sys

input = sys.stdin.readline

def count_square_free_numbers(min_val, max_val):
    import math
    
    range_len = max_val - min_val + 1
    is_square_free = [True] * range_len
    
    limit = int(math.sqrt(max_val)) + 1
    
    for i in range(2, limit):
        square = i * i
        start = max(square, (min_val + square - 1) // square * square)
        
        for j in range(start, max_val + 1, square):
            is_square_free[j - min_val] = False
    
    return sum(is_square_free)

min_val, max_val = map(int, input().strip().split())
print(count_square_free_numbers(min_val, max_val))