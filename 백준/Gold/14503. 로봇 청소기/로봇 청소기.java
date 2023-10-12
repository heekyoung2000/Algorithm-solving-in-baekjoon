import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;




class Main {
    static int N, M, x, y;
    static int d;
    static int[][] map;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(bfs(x, y, d));

    }

    public static int bfs(int x, int y, int d) {
        int cnt = 0;
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(x, y, d));

        while (!queue.isEmpty()) {
            Point p = queue.poll();
            if (map[p.x][p.y] == 0) {// 현재 칸이 청소가 되지 않은 경우
                map[p.x][p.y] = 2;
                cnt++;
            }
            boolean check = false;
            for (int i = 0; i < 4; i++) {
                int n_d = (p.d + 3) % 4;//왼쪽방향으로 회전
                int n_x = p.x + dx[n_d];
                int n_y = p.y + dy[n_d];

                if (n_x >= 0 && n_x < N && n_y >= 0 && n_y < M && map[n_x][n_y] == 0) {//현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
                    queue.add(new Point(n_x, n_y, n_d));
                    check = true;
                    break;
                }
                p.d = n_d;
            }
            if (!check) { //주변 4칸이 청소되지 않은 빈칸이 없는 경우
                int backDir = (p.d + 2) % 4;
                int back_x = p.x + dx[backDir];
                int back_y = p.y + dy[backDir];



                if (map[back_x][back_y]!=1) {
                    queue.add(new Point(back_x, back_y, p.d));
                }
            }

        }

        return cnt;
    }

}

class Point {
    int x;
    int y;
    int d;

    Point(int x, int y, int d) {
        this.x = x;
        this.y = y;
        this.d = d;
    }

}
