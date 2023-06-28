import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      

        int N = Integer.parseInt(br.readLine());
        Integer[] num_list = new Integer[N];
        int sum=0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            int num = Integer.parseInt(st.nextToken());
            num_list[i]=num;
        }
        Arrays.sort(num_list);
        for(int i=1; i<N; i++){
            num_list[i]=num_list[i-1]+num_list[i];
        }
        for(int j=0;j<N;j++){
            sum+= num_list[j];
        }
        System.out.println(sum);
    }
    
}
