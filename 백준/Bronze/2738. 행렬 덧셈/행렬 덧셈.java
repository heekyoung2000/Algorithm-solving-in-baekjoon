import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out)); 


        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int array1[][]=new int[N][M];
        int array2[][]=new int[N][M];

        for(int i =0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                array1[i][j]=Integer.parseInt(st.nextToken());

            }
        }

        for(int i =0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                array2[i][j]=Integer.parseInt(st.nextToken());

            }
        }

        for(int i =0; i<N; i++){
            for(int j=0; j<M; j++){
                //print는 줄바꿈을 하지 않고 println은 줄바꿈이 있음
                System.out.print(array1[i][j]+array2[i][j]+" ");
                if(j==M-1){
                    System.out.println();
                }
            }
        }
    }
}
