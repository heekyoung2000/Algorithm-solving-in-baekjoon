import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> nArrayList = new ArrayList<>();
        for(int i=0;i<n;i++){
            int num = Integer.parseInt(br.readLine());
            nArrayList.add(num);
        }
        Collections.sort(nArrayList);

        for(int value : nArrayList){
            sb.append(value).append('\n');
        }
        System.out.println(sb);
    }
    
}