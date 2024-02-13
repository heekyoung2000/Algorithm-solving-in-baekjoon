def solution(citations):
    k=len(citations)
    
    def s(arr): #정렬 구현
        n=len(citations)
        a=0
        while a<n-1:
            last=n-1
            for j in range(n-1,a,-1):
                if arr[j-1]>arr[j]:
                    arr[j-1],arr[j]=arr[j],arr[j-1]
                    last=j
            n=last
        return arr
    
    def sorted(new_arr):
        result=[]
        s(new_arr)
        left=0
        right=new_arr[-1]
        while left<right:
            mid=(left+right)//2
            count=0
            left_count=0
            for r in new_arr:
                if r>=mid:
                    count+=1
                else:
                    left_count+=1   
            #mid번 이상 인용된 논문이 mid편이상 & 나머지 논문이 mid 이하 
            if count==mid and left_count==k-count:
                result.append(mid)
                left+=1
            elif count<mid:#mid번 이상 인용된 논문이 mid편 미만일 경우
                right-=1
            else:#mid번 이상 인용된 논문이 mid편 초과일 경우
                left+=1
        if result==[]:
            return left-1
        else:
            return result[-1]
            
    
    
    if k==1:
        if citations[0]==1:
            return 1
        else:
            return 0
    elif len(set(citations))==1:
        return citations[0]
    else:
        return sorted(citations)
        