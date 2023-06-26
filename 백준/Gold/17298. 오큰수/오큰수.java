import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        // Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        int N = Integer.parseInt(br.readLine());
        int A[] = new int[N];
        int ans[] = new int[N];
       
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<N; i++){
            A[i]=Integer.parseInt(st.nextToken());
        }

        Stack<Integer> stackInt = new Stack<>(); // Integer형 스택 선언
        stackInt.push(0);

        for(int i=1;i<N;i++){
            while(!stackInt.isEmpty() && A[stackInt.peek()]<A[i] ){
                ans[stackInt.pop()]=A[i];
            }
            stackInt.push(i);
        }
        
        while(!stackInt.isEmpty()){
            ans[stackInt.pop()]=-1;

        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i=0;i<N; i++){
            bw.write(ans[i]+" ");
        }
        bw.write("\n");
        bw.flush();
    
    }
    
}
