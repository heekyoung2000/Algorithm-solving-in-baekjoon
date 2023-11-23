from collections import deque
def solution(begin, target, words):
    answer=0
    if target not in words:
        return answer
    else:
        return bfs(begin,words,target)
    
def bfs(word,words,target):
    q = deque()
    q.append([word,0])
    while q:
        wor,answer= q.popleft()
        if wor == target:
            return answer
        for w in words:
            count=0
            for l in range(len(w)):
                if w[l]!= wor[l]:
                    count+=1
            if count==1:
                q.append([w,answer+1])
                
    
    
    