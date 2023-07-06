import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] A;
    static boolean result;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        

        int N = Integer.parseInt(br.readLine());
        A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        for(int i =0; i< N; i++){
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine()," ");

        StringBuilder sb = new StringBuilder();
        for(int i=0; i<M;i++){
            if(find(Integer.parseInt(st.nextToken()))!=-1){
                sb.append(1).append('\n');
            }
            else{
                sb.append(0).append('\n');
            }
        }
        System.out.println(sb);
    }
    private static int find(int key) {
        int lo = 0;
        int high = A.length-1;
        while(lo<=high){
            int mid= (lo+high)/2;
            if(key<A[mid]){
                high = mid-1;
            }
            else if(key>A[mid]){
                lo=mid+1;
            }
            else{
                return mid;
            }

        }
        return -1;
    }
}
