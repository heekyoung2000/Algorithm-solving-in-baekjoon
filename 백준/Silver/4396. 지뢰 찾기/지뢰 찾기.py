from sys import stdin as s

#s=open("input.txt")

n=int(s.readline())

star_list=[]
x_list=[]
comma_list=[]
dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]
bump=False

for _ in range(n):
    list1=list(s.readline().strip())
    star_list.append(list1)

for _ in range(n):
    list1=list(s.readline().strip())
    x_list.append(list1)


def search(x,y):
    cnt=0
    # if star_list[x][y]=="*":
    #     cnt+=1
    for i in range(8):
        new_x=x+dy[i]
        new_y=y+dx[i]
        if 0<=new_x<n and 0<=new_y<n:
            if star_list[new_x][new_y]=='*':
                cnt+=1
    return cnt


    
p=0
q=0    
for i in range(n):
    for j in range(n):
        if x_list[i][j]=='x':
            if star_list[i][j]=='*' and bump==False:
                x_list[i][j]=search(i,j)
                p+=i
                q+=j
                bump=True
            else:
                x_list[i][j]=search(i,j)
        

if bump==True:                
    for i in range(n):
        for j in range(n):
            # if i==p and j==q:
            #     continue
            if star_list[i][j]=="*":
                x_list[i][j]="*"
count=0
for z in x_list:
    for a in z:
        if a=="x":
            a=0
        count+=1
        print(a,end="")
        if count==n:
            print()
            count=0