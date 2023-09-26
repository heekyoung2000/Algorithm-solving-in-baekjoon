def solution(answers):
    number1 = [1,2,3,4,5] #5
    number2 = [2,1,2,3,2,4,2,5] #8
    number3 = [3,3,1,1,2,2,4,4,5,5] #10
    result=[0]*3
    answer=[]
    for i in range(len(answers)):
        if answers[i]==number1[i%5]:
            result[0]+=1
        if answers[i]==number2[i%8]:
            result[1]+=1
        if answers[i]==number3[i%10]:
            result[2]+=1
            
    winner = max(result)
    for i in range(len(result)):
        if result[i]==winner:
            answer.append(i+1)
    return answer
    
    
    
    
                    
                