S = list(map(str,input()))
new_list=[]
new_num = ""

for i in range(len(S)-1,-1,-1):
    new_num = S[i]+new_num
    new_list.append(new_num)


new_list=sorted(new_list)
for i in new_list:
    print(i)