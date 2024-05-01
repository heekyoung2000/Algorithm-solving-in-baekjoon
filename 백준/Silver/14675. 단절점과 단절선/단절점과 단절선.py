import sys
input =sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q= int(input())
for _ in range(q):
    t,k = map(int,input().split())
    #t=1는 단절점,t=2는 단절선
    if t==1:
        if(len(graph[k])<2):
            print("no")
        else:
            print("yes")
    elif t==2:
        print("yes")
    
