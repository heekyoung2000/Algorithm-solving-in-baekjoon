import sys
input = sys.stdin.readline

N,K =map(int,input().split())

hour = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
minute=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"
        ,"30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]

second=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"
        ,"30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
#시간 : 00시~N시
#분 : 00~60분
#초 : 00~60초

cnt=0

for h in hour[:N+1]:
    list_h = list(map(str,h))
    for m in minute:
        list_m = list(map(str,m))
        for s in second:
            list_s = list(map(str,s))
            if str(K) in list_h or str(K) in list_m or str(K) in list_s:
                cnt+=1
        
print(cnt)