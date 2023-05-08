import sys

#s=open("input.txt","rt")


def again(num,start,kantoa):
    if num==1:
        return kantoa
    else:
        num=num//3
        again(num,start,kantoa)
        for i in range(start+num,start+num*2):
            kantoa[i]=" "
        again(num,start+num*2,kantoa)
        
while True:
    try:       
        n=int(sys.stdin.readline().strip())
        num=3**n
        kantoa = ['-']*(num)
        answer=""
        again(num,0,kantoa)
        print(''.join(kantoa))
    except:
        break