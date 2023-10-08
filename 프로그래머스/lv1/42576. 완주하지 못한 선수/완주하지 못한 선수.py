def solution(participant, completion):
    # answer = ''
    # participant.sort()
    # completion.sort()
    # for j in range(len(completion)):
    #     if participant[j]!=completion[j]:
    #         return participant[j]
    # return participant[len(participant)-1]
    hashDict={}
    sumHash = 0
    
    for part in participant:
        hashDict[hash(part)]=part
        sumHash+= hash(part)
        
    for comp in completion:
        sumHash -= hash(comp)
        
    return hashDict[sumHash]