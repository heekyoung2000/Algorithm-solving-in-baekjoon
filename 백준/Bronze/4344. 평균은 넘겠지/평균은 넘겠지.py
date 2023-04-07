c = int(input())

for i in range(c):
    num=0
    score = list(map(int, input().split()))
    score.pop(0)
    for j in score:
        avg = sum(score)//len(score)
        if j>avg:
            num+=1
    result = format(num/len(score)*100,".3f")
    print(f'{result}%')
        