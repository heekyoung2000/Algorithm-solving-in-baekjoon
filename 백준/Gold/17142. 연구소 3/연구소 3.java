import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    static int N, M;
    static int[][] map;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static int count;
    static int min = Integer.MAX_VALUE;
    static ArrayList<P> virusPoint;


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        count = N*N;

        map = new int[N][N];
        virusPoint = new ArrayList<>();

        for(int i=0; i<N; i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                map[i][j]=Integer.parseInt(st.nextToken());

                if(map[i][j]==1) count--;
                if(map[i][j] == 2){
                    count--;
                    virusPoint.add(new P(i,j));
                }

            }
        }
        if(count==0){
            System.out.println(0);
        }else{
            dfs(0,0);
            System.out.println(min != Integer.MAX_VALUE ? min : -1);
        }
    }
    public static void dfs(int depth,int start){
        if(depth==M){
            bfs();
            return;
        }else{
            for(int i = start; i< virusPoint.size(); i++){
                P p = virusPoint.get(i);

                map[p.x][p.y]=3; // 바이러스 활성화
                dfs(depth+1, i+1);
                map[p.x][p.y] =2;
            }
        }
    }
    public static void bfs(){ // bfs로 바이러스를 퍼뜨림
        Queue<P> queue = new LinkedList<>();
        int[][] visited = new int[N][N];

        int[][] copyMap = new int[N][N];

        for(int i=0; i< N; i++){
            for(int j=0; j<N; j++){
                copyMap[i][j] = map[i][j];

                if(copyMap[i][j]==3){
                    queue.add(new P(i,j));
                    visited[i][j] = 1;
                }
            }
        }
        int cnt = 0; //바이러스가 퍼진 칸의 개수를 저장

        while(!queue.isEmpty()){
            int cx = queue.peek().x;
            int cy = queue.poll().y;

            for(int i =0; i< 4; i++){
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                //범위 벗어나거나 벽이라면 퍼뜨릴 수 없음
                if(nx <0 || ny<0 || nx>=N || ny>= N || copyMap[nx][ny]==1){
                    continue;
                }
                if(visited[nx][ny]==0){
                    visited[nx][ny] = visited[cx][cy]+1;
                    queue.add(new P(nx,ny));

                    if(copyMap[nx][ny]==0) cnt++; //비활성바이러스를 활성화 시킨 경우 포함 x
                    if(cnt == count){
                        min=Math.min(min, visited[nx][ny]-1);
                    }
                }
            }
        }
    }


}
class P{
    int x;
    int y;
    P(int x, int y){
        this.x = x;
        this.y = y;
    }

}