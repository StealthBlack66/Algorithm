def find_sequence(N, A):
    indexed_A = [(A[i], i) for i in range(N)]
    indexed_A.sort()
    P = [0] * N
    for new_index, (value, original_index) in enumerate(indexed_A):
        P[original_index] = new_index
    
    return P

N = int(input())
A = list(map(int, input().split()))
P = find_sequence(N, A)
print(*P)