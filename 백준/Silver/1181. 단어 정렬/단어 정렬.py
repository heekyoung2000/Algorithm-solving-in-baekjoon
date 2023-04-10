import sys
    
n=int(sys.stdin.readline())
list1=[]
new_list=[]    
for i in range(n):
    word = str(sys.stdin.readline().strip())
    length= len(word)
    new_list.append([word,length])
list1 = set(list(map(tuple,new_list)))
new_list=list(list1)
new_list.sort(key=lambda new_list:(new_list[1],new_list))
for i in list(new_list):
    print(i[0])