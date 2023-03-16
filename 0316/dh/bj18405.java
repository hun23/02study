import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;


class Pair {
	int r, c;
	Pair(int r, int c) {
		this.r = r;
		this.c = c;
	}
}

public class bj18405 {
	public static void run() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		// get input N, K
		String[] nk = br.readLine().split(" ");
		int N = Integer.parseInt(nk[0]);
		int K = Integer.parseInt(nk[1]);
		// make arr, time_passed, hashmap for virus
		int[][] arr = new int[N][N];
		int[][] time_passed = new int[N][N];
		HashMap<Integer, ArrayList<Pair>> map = new HashMap<>();
		// initiate Hashmap
		int i;
		int j;
		for (i = 1; i < K + 1; i++) {
			map.put(i, new ArrayList<Pair>());
		}
		// get input
		for (i = 0; i < N; i++) {
			String[] inp = br.readLine().split(" ");
			for (j = 0; j < N; j++) {
				int num = Integer.parseInt(inp[j]);
				arr[i][j] = num;
				if (num == 0) {
					time_passed[i][j] = -1;
				} else {
					time_passed[i][j] = 0;
				}
				if (arr[i][j] != 0) {
					map.get(arr[i][j]).add(new Pair(i, j));
				}
			}
		}
		// get S, X, Y
		String[] SXY = br.readLine().split(" ");
		int S = Integer.parseInt(SXY[0]);
		int X = Integer.parseInt(SXY[1]);
		int Y = Integer.parseInt(SXY[2]);

		// put virus coordinates in queue
		Queue<Pair> queue = new LinkedList<>();
		for (i = 1; i < K + 1; i++) {
			queue.addAll(map.get(i));
		}
		
		// BFS
		bfs(arr, time_passed, queue, S);
		bw.write(String.valueOf(arr[X - 1][Y - 1]));
		bw.flush();
		bw.close();
	}

	static void bfs(int[][] arr, int[][] time_passed, Queue<Pair> queue, int S) {
		int[] dr = {1, 0, -1, 0};
		int[] dc = {0, 1, 0, -1};
		int i;
		while (!queue.isEmpty()) {
			Pair cur = queue.poll();
			for (i = 0; i < 4; i++) {  // check 4 directions
				int nr = cur.r + dr[i];
				int nc = cur.c + dc[i];
				if (arr.length > nr && nr >= 0) {
					if (arr.length > nc && nc >= 0) {  // in index range
						// when time is not over & cell is empty
						if (time_passed[cur.r][cur.c] + 1 <= S && arr[nr][nc] == 0) {
							queue.add(new Pair(nr, nc));
							// update time_passed & arr
							time_passed[nr][nc] = time_passed[cur.r][cur.c] + 1;
							arr[nr][nc] = arr[cur.r][cur.c];
						}
					}
				}
			}
		}
	}
}