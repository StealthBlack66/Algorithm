import sys
input = sys.stdin.readline
output = sys.stdout.write

# 테스트케이스의 개수 T 입력
T = int(input().strip())

results = []
for _ in range(T):
    # 각 줄에 두 정수 A와 B가 주어짐
    A, B = map(int, input().strip().split())
    # 결과를 리스트에 저장
    results.append(A + B)

# 결과를 한꺼번에 출력
output('\n'.join(map(str, results)) + '\n')
