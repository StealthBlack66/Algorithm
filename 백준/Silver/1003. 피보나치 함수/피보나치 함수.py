def count_fibonacci_calls(n):
    dp_zero = [0] * (n + 1)
    dp_one = [0] * (n + 1)
    if n >= 0:
        dp_zero[0] = 1
        dp_one[0] = 0
    if n >= 1:
        dp_zero[1] = 0
        dp_one[1] = 1
    for i in range(2, n + 1):
        dp_zero[i] = dp_zero[i - 1] + dp_zero[i - 2]
        dp_one[i] = dp_one[i - 1] + dp_one[i - 2]
    
    return dp_zero[n], dp_one[n]

T = int(input())
test_cases = [int(input()) for _ in range(T)]

for n in test_cases:
    zero_count, one_count = count_fibonacci_calls(n)
    print(zero_count, one_count)
