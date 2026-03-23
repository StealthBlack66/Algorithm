from collections import deque
import sys

class BinaryHeap:
    def __init__(self):
        self._heap = []
    def _perc_up(self,cur):
        while (cur-1)//2>= 0:
            parent = (cur-1)//2  
            if self._heap[cur] < self._heap[parent]:
                self._heap[cur],self._heap[parent] = (self._heap[parent], self._heap[cur])
            cur = parent

    def _perc_down(self,cur):
        while (cur*2+1)<len(self._heap):
            min_child = self._get_min_child(cur)
            if self._heap[cur] > self._heap[min_child]:
                self._heap[cur], self._heap[min_child] = (self._heap[min_child], self._heap[cur])
            else: return
            cur = min_child

    def _get_min_child(self,cur):
        if cur*2+2 > len(self._heap)-1:
            return cur*2+1
        if self._heap[cur*2+1] <= self._heap[cur*2+2]:
            return cur*2+1
        else:
            return cur*2+2
        
    def heapify(self,not_heap):
        self._heap = not_heap
        cur = len(self._heap)//2-1
        while cur >= 0:
            self._perc_down(cur)
            cur = cur-1

    def get_min(self):
        return self._heap[0]

    def insert(self,item):
        self._heap.append(item)
        self._perc_up(len(self._heap)-1)

    def delete(self):
        self._heap[0],self._heap[-1] = self._heap[-1],self._heap[0]
        dele = self._heap.pop()
        self._perc_down(0)
        return dele
    
    def is_empty(self):
        return not bool(self._heap)

    def __len__(self):
        return len(self._heap)
               
    def __str__(self):
        return str(self._heap)

input = sys.stdin.readline
N = int(input())
my_heap = BinaryHeap()
for _ in range(N):
    x = int(input())
    if x == 0:
        if my_heap.is_empty():
            print(0)
        else:
            print(my_heap.delete())
    else:
        my_heap.insert(x)