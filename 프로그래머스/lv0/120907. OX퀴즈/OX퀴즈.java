import java.util.ArrayList;

class Solution {
    
    public String[] solution(String[] quiz) {
String [] arr = new String[quiz.length];
        for(int i=0;i<quiz.length;i++){
            String[] answer = quiz[i].split(" ");
            int num1=Integer.parseInt(answer[0]);
            int num2=Integer.parseInt(answer[2]);
            int result = Integer.parseInt(answer[4]);
            int ans=0;
            if(answer[1].equals("-")){
                if((num1-num2)==result){
                   arr[i]="O"; 
                }
                else{
                    arr[i]="X";
                }
            }
            if(answer[1].equals("+")){
                if((num1+num2)==result){
                   arr[i]="O"; 
                }
                else{
                    arr[i]="X";
                }
            }
        }
        return arr;
    }
}