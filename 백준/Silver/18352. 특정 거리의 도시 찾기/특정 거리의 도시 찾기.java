import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer> A[];
    static int N;
    static int M;
    static int k;
    static int x;
    static boolean visited[];
    static int go_list[];
    static List<Integer> answer;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        answer = new ArrayList<>();
        visited = new boolean[N+1];

        A = new ArrayList[N+1];
        for(int i=1; i<=N; i++){
            A[i]=new ArrayList<Integer>();
        }

        for(int i=0;i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            A[a].add(b);
        }

        go_list = new int[N+1];
        for(int i=0; i<=N;i++){
            go_list[i]=-1;
        }

       
        BFS(x);
        for(int i=0; i<=N; i++){
            if(go_list[i]==k){
                answer.add(i);   
            }
        }
        
        if(answer.isEmpty()){
            System.out.print("-1");
        }
        else{
            Collections.sort(answer); //collections과 array의 차이를 잘 모르겠음.
            for(int a: answer){
                System.out.println(a);
            }   
        }
    }
    private static void BFS(int node){
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(node);
        go_list[node]++;

        while(!queue.isEmpty()){
            int now_node = queue.poll();
            for(int i: A[now_node]){
                if(go_list[i]==-1){
                    go_list[i]=go_list[now_node]+1;
                    queue.add(i);
                }
            }
        }
    }
}
