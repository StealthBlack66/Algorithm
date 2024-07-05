arr=list(range(1,31))
for i in range(28):
    a=int(input())
    arr.remove(a)
print('\n'.join(map(str,arr)))