import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
my_deque = deque([])

for i in range(T):
    context = list(input().split())
    if context[0] not in ['push_front','push_back','pop_front','pop_back','size','empty','front','back']:
        break
    if context[0] == 'push_front':
        my_deque.append(context[1])
    elif context[0] == 'push_back':
        my_deque.appendleft(context[1])
    elif context[0] == 'pop_front':
        print(my_deque.pop() if my_deque else -1)
    elif context[0] == 'pop_back':
        print(my_deque.popleft() if my_deque else -1)
    elif context[0] == 'size':
        print(len(my_deque))
    elif context[0] == 'empty':
        print(0 if my_deque else 1)
    elif context[0] == 'front':
        print(my_deque[-1] if my_deque else -1)
    elif context[0] == 'back':
        print(my_deque[0] if my_deque else -1)