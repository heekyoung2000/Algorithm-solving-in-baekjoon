import sys
T= int(sys.stdin.readline().strip())
for i in range(T):
    n = int(sys.stdin.readline().strip())
    number_list=sorted([sys.stdin.readline().strip() for _ in range(n)])
    for j in range(n-1):
        if number_list[j]==number_list[j+1][:len(number_list[j])]:
            #number_list 첫번째 값과 다음 값을 비교할때, 다음값에서 처음부터 이전값의 길이까지 비교를 했을 때 똑같으면 일관성 없음
            print("NO")
            break
    else:
        print("YES")