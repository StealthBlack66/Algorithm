import sys
input = sys.stdin.readline

N = int(input())
expression = input().strip()

nums = []
ops = []

# 파싱
for i in range(N):
    if i % 2 == 0:
        nums.append(int(expression[i]))
    else:
        ops.append(expression[i])

def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

answer = -int(1e9)

def dfs(idx, current):
    global answer
    
    if idx == len(ops):
        answer = max(answer, current)
        return
    
    # 괄호 없이
    dfs(idx+1, calc(current, ops[idx], nums[idx+1]))
    
    # 괄호 사용
    if idx + 1 < len(ops):
        bracket = calc(nums[idx+1], ops[idx+1], nums[idx+2])
        dfs(idx+2, calc(current, ops[idx], bracket))

dfs(0, nums[0])

print(answer)