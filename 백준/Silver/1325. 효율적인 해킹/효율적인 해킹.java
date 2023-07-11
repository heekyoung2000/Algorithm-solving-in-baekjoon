import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static ArrayList<Integer> A[];
    static boolean visited[];
    static int result[];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        A = new ArrayList[N+1];
        result = new int[N+1];

        for(int i=0; i<N+1; i++){
            A[i] = new ArrayList<Integer>();
        }

    
        for(int j=0; j<M; j++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            A[a].add(b);
        }   

        for(int i=0;i<N+1;i++){
            visited= new boolean[N+1];
            DFS(i);
        }


        int cnt=0;
        for(int i=1; i<N+1; i++){
            cnt = Math.max(cnt,result[i]);
        }

        for(int i =1; i<N+1; i++){
            if(result[i]==cnt){
                System.out.print(i+" ");
            }
        }

    }
    private static void DFS(int node) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(node);
        visited[node] = true;
        
        while(!queue.isEmpty()){
            int now_node =queue.poll();
            for(int k:A[now_node]){
                if(visited[k]==false){
                    visited[k]=true;
                    result[k]++;
                    queue.add(k);
                    
                }
            }
        }

        

    }
}