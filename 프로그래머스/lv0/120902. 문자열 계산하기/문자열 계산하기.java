class Solution {
    public int solution(String my_string) {
        String []arr = my_string.split(" ");
        int num1 = Integer.parseInt(arr[0]);
        int result;
        
        for(int i=0; i<arr.length;i++){
            if(arr[i].equals("+")){
                num1+=Integer.parseInt(arr[i+1]);
            }
            else if(arr[i].equals("-")){
                num1-=Integer.parseInt(arr[i+1]);
            }
        }
       
        return num1;
       
    }
}