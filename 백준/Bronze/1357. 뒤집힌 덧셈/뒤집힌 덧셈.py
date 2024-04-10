import sys
from collections import deque
input = sys.stdin.readline

num_list=list(map(str,input()))
q=deque()
s_num=0
for num in num_list:
    if num==" " or num=="\n":
        s=""
        while q:
            s+=q.popleft()
        s_num+=int(s)
        continue
    else:
        q.appendleft(num)
result_list=list(map(str,str(s_num)))
result=""
for r in reversed(result_list):
    result+=r
    
print(int(result))


