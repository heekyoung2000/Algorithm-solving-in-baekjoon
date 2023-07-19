import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String str = br.readLine();
        String bump = br.readLine();

        Stack<Character> leftSt = new Stack<>();

        int stack_size = str.length();
        int bump_size = bump.length();

        for (int i = 0; i < stack_size; i++) {
            int count = 0;
            leftSt.push(str.charAt(i));
            if (leftSt.size() >= bump_size) {
                for (int j = 0; j < bump_size; j++) {
                    if (leftSt.get(leftSt.size() - bump_size + j) == bump.charAt(j)) {
                        count++;
                    }
                    if (count == bump_size) {
                        for (int a = 0; a < bump_size; a++) {
                            leftSt.pop();
                        }
                    }
                }

            }

        }

        if (leftSt.isEmpty()) {
            System.out.println("FRULA");
        } else {
            for (char ch : leftSt) {
                sb.append(ch);
            }
            
        }
        System.out.println(sb);
    
    }

}
