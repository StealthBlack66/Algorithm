import sys, queue

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
my_stack = queue.LifoQueue()

def push(st,item):
    st.put(item)

def pop(st):
    if st.qsize() <= 0:
        return -1
    else:
        return st.get()

def size(st):
    return st.qsize()

def empty(st):
    if st.qsize() <= 0:
        return 1
    else:
        return 0 

def top(st):
    if st.qsize() <= 0:
        return -1
    else: return st.queue[-1]

for i in range(T):
    context = list(input().split())
    if context[0] not in 'push pop size empty top':
        break 
    if context[0] == 'push':
        push(my_stack, context[1])
    elif context[0] == 'pop':
        print(pop(my_stack))
    elif context[0] == 'size':
        print(size(my_stack))
    elif context[0] == 'empty':
        print(empty(my_stack))
    elif context[0] == 'top':
        print(top(my_stack))