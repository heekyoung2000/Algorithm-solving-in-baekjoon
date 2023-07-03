import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] A;
    static boolean[] visited;
    static boolean arrive;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        arrive =false;
        A = new ArrayList[N];
        visited = new boolean[N];
        for(int i=0; i<N; i++){
            A[i]=new ArrayList<Integer>();
        }
        
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            A[a].add(b);
            A[b].add(a);
        }

        for(int i=0; i<N; i++){
            DFS(i,1);
            if(arrive)
                break;
            
        }
        if(arrive){
            System.out.println("1");
        }
        else{
            System.out.println("0");
        }
    }
    static void DFS(int v,int depth){
        if(depth==5 || visited[v]){
            arrive=true;
            return;
        }
        visited[v]=true;
        for(int i: A[v]){
            if(visited[i]==false)
                DFS(i,depth+1);
        }
        visited[v] = false;
    }

}