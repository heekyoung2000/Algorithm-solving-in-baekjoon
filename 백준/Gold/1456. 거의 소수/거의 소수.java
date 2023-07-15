import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
         
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());

        long num_array[] = new long[10000001];
        for(int i=2; i<num_array.length; i++){
            num_array[i] = i; //초기화
        }
        for(int i=2; i<=Math.sqrt(num_array.length); i++){
            if(num_array[i]==0){
                continue;
            }
            for(int j=i+i; j<num_array.length; j=j+i){
                num_array[j]=0;
            }
        }

        
        int count=0;    
        for(int j=2; j<10000001; j++){
            if(num_array[j]!=0){
                long temp = num_array[j];
                while((double)num_array[j] <= (double)B/(double)temp){
                    if((double)num_array[j] >= (double)A/(double)temp)
                        count++;
                    temp=temp*num_array[j];
                }
                
            }

        }
        System.out.println(count);
    
    }
    
}
