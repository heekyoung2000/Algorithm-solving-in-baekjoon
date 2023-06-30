import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    
    static int N;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N= Integer.parseInt(br.readLine());
        DFS(2,1);
        DFS(3,1);
        DFS(5,1);
        DFS(7,1);

    }
    static void DFS(int n,int i){
        if(i==N){
            System.out.println(n);
        }
        
        else{
            for(int j=1;j<10;j++){
                if(j%2!=0 && isPrime(n*10+j)){ // 소수라면 재귀 함수로 자릿수 늘림
                    DFS(n*10+j,i+1);
                }
            }
        }

    }
    static boolean isPrime (int num) {
        for(int a=2; a<=num/2; a++)
            if(num%a==0)
                return false;
            return true;
    }
}
