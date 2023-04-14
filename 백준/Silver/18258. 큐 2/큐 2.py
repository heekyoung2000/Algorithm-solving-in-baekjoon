import sys
from collections import deque

queue = deque()
data = int(sys.stdin.readline())

for _ in range(data):
    n = sys.stdin.readline().split()
    
    if n[0] == 'push':
        queue.append(int(n[1]))
        
    elif n[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
            
    elif n[0] == 'size':
        print(len(queue))
    elif n[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    
    elif n[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            
    elif n[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])