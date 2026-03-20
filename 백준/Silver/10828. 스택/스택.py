import sys, queue

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
my_stack = []

for i in range(T):
    context = list(input().split())
    if context[0] not in ['push', 'pop', 'size', 'empty', 'top']:
        break 
    if context[0] == 'push':
        my_stack.append(context[1])
    elif context[0] == 'pop':
        print(my_stack.pop() if my_stack else -1)
    elif context[0] == 'size':
        print(len(my_stack))
    elif context[0] == 'empty':
        print(0 if my_stack else 1)
    elif context[0] == 'top':
        print(my_stack[-1] if my_stack else -1)