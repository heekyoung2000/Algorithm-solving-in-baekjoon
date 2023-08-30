from sys import stdin as s
from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(index,selected):
    if len(selected)==6:
        #6개의 숫자가 선택되었을 때 출력
        print(' '.join(map(str, selected)))
        return
    
    if index >= len(numbers):
        return
    #index와 같은 numbers 추가 후 재귀
    dfs(index+1, selected + [numbers[index]])
    #index외의 numbers 재귀
    dfs(index+1, selected)
    
    
while True: 
   k, *numbers = map(int,s.readline().split())
   if k==0:
       break
   dfs(0,[])
   print()
   

    