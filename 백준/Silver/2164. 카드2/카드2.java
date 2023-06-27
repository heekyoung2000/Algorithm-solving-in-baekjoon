import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        int N = Integer.parseInt(br.readLine());
        
        Deque<Integer> dq = new ArrayDeque<>();

        for(int i =1; i<N+1; i++){
            dq.offer(i);
        }
        while(dq.size()>1){
            dq.poll();
            int card = dq.poll();
            dq.offerLast(card);
        }

    
        System.out.println(dq.poll());
        
    }
    
}
