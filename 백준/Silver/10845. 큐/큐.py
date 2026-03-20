from collections import deque
import sys
#sys.stdin = open('open.txt', 'r')

input = sys.stdin.readline

T = int(input())
my_queue = deque([])

for i in range(T):
    state = list(input().split())

    if state[0] not in ['push', 'pop','size','empty','front','back']:
        break
    if state[0] == 'push':
        my_queue.appendleft(state[1])
    elif state[0] == 'pop':
        print(my_queue.pop() if my_queue else -1)
    elif state[0] == 'size':
        print(len(my_queue))
    elif state[0] == 'empty':
        print(0 if my_queue else 1)
    elif state[0] == 'front':
        print(my_queue[-1] if my_queue else -1)
    elif state[0] == 'back':
        print(my_queue[0] if my_queue else -1)