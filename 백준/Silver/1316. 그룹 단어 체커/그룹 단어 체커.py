t=int(input())
answer=0
for i in range(t):
    new_word = list(map(str,input()))
    result=False
    while len(new_word)!=0:
        n_w = new_word.pop()
        if n_w in new_word:
            if n_w !=new_word[-1]:
                result=False
                break
        else:
            result=True
    if result==True:
        answer+=1
    
print(answer)