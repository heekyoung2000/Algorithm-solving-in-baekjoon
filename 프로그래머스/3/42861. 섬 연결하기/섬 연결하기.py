def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    
    graph = [i for i in range(n)]
    room = [[i] for i in range(n)]
    answer = 0
    made = 0
    
    for x,y,cost in costs:
        x= graph[x]
        y= graph[y]
        
        if x==y: continue
        while room[y]:
            k = room[y].pop()
            room[x].append(k)
            graph[k]=x
        answer+= cost
        made+=1
        if made == n-1:
            break
    return answer