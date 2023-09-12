import java.util.Arrays;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);
        for(int i=0;i<reserve.length;i++){
            for(int j=0;j<lost.length;j++){
                if(lost[j]==reserve[i]){
                    reserve[i]=123;
                    lost[j]=123;
                }
            }
        }
        int num=0;
        for(int r=0; r<lost.length; r++){
            if(lost[r]<=30){
                num+=1;
            }
        }
        int answer = n-num;
        for(int a=0;a<lost.length;a++){
            for(int b=0;b<reserve.length;b++){
                if(lost[a]-1==reserve[b] || lost[a]+1==reserve[b]){
                    answer+=1;
                    lost[a]=-1;
                    reserve[b]=-999;
                    break;
                }
            }
        }
        return answer;
    }
}