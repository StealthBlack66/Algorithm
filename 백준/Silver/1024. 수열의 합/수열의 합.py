def find_sequence(N, L):
    for length in range(L, 101):
        if (2 * N + length - length**2) % (2 * length) == 0:
            a = (2 * N + length - length**2) // (2 * length)
            if a >= 0:
                return list(range(a, a + length))
    return -1

N, L = map(int, input().split())

result = find_sequence(N, L)
if result == -1:
    print(result)
else:
    print(*result)