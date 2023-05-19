from sys import stdin as s

#s=open("input.txt","rt")

n=list(map(str,s.readline().strip())) 
num_list = ['0','1','2','3','4','5','6','7','8','9']
cnt=1
dp=[1 for _ in range(10)]

def check(i):
    if i=='6' and i not in num_list and '9' in num_list:
        num_list.remove('9')
    elif i=='9' and i not in num_list and '6' in num_list:
        num_list.remove('6')
    else:
        num_list.remove(i)
    
for i in n:
    if i=='6' and i not in num_list and '9' in num_list:
        num_list.remove('9')
    elif i=='9' and i not in num_list and '6' in num_list:
        num_list.remove('6')
    elif i in num_list:
        num_list.remove(i)
    else:
        num_list=['0','1','2','3','4','5','6','7','8','9']
        check(i)
        if i=='6' or i=='9':
            dp[int(6)]+=1
        else:
            dp[int(i)]+=1
print(max(dp))
        