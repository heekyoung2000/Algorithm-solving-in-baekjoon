import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int total = 0;
        int n = Integer.parseInt(br.readLine()); // 색종이 개수
        boolean[][] arr= new boolean[101][101]; // 도화지

        for(int i =0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            for(int j = a; j<a+10; j++){
                for(int k = b; k< b+10; k++){
                    if(!arr[j][k]){
                        arr[j][k]=true;
                        total++;
                    }
                }
            }
        }
        System.out.println(total);


    }
}
