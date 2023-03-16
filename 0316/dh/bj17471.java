import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;


public class bj17471 {
    public void run() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        String[] inp = br.readLine().split(" ");
        int answer = Integer.MAX_VALUE;

        // get populations
        int[] populations = new int[N];
        int i;
        int j;
        for (i = 0; i < N; i++) {
            populations[i] = Integer.parseInt(inp[i]);
        }

        // make adjacent List
        int[][] adjL = new int[N][N];
        for (i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            int M = Integer.parseInt(temp[0]);
            for (j = 1; j < M + 1; j++) {
                int num = Integer.parseInt(temp[j]);
                adjL[i][num - 1] = 1;
            }
        }

        // get subset
        for (i = 0; i < (1 << N); i++) {
            int[] groups = new int[N];
            for (j = 0; j < N; j++) {
                if ((i & (1 << j)) != 0) {
                    groups[j] = 1;
                }
            }
            // BFS
            int this_case = bfs(adjL, populations, groups);
            if (this_case != -1 && this_case < answer) {
                answer = this_case;
            }

        }
        // print answer
        if (answer != Integer.MAX_VALUE) {
            bw.write(String.valueOf(answer));
        } else {
            bw.write(String.valueOf(-1));
        }
        bw.flush();
        bw.close();
    }

    static int bfs(int[][] adjL, int[] populations, int[] groups) {
        int i;
        int j;
        int k;
        int sum = 0;
        boolean[] visited = new boolean[groups.length];
        for (i = 0; i < 2; i++) {
            Queue<Integer> queue = new LinkedList<>();
            for (j = 0; j < groups.length; j++) {
                if (groups[j] == i) {
                    queue.add(j);
                    break;
                }
            }
            while (!queue.isEmpty()) {
                int cur = queue.poll();
                sum += (i == 0) ? populations[cur] : (-1 * populations[cur]);
                visited[cur] = true;
                for (j = 0; j < adjL[cur].length; j++) {
                    if (adjL[cur][j] == 1) {  // if next node exists
                        if (groups[j] == i && !visited[j]) {  // in same group & not visited
                            visited[j] = true;
                            queue.add(j);
                        }
                    }
                }
            }
            for (k = 0; k < groups.length; k++) {
                if (groups[k] == i && !visited[k]) {
                    return -1;
                }
            }
        }
        return (sum > 0) ? sum : -1 * sum;
    }
}