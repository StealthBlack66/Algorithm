import sys
input = sys.stdin.readline
output = sys.stdout.write

# 테스트케이스의 개수 T 입력
T =int(input().strip())

for i in range(T):
    # 각 줄에 두 정수 A와 B가 주어짐
    A, B = map(int, input().strip().split())
    output(f'Case #{i+1}: {A} + {B} = {A+B}\n')