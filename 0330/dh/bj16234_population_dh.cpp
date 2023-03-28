#include <iostream>
#include <stdlib.h>  // malloc, abs
#include <queue>
#include <memory.h>  // memset

int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

int main(void)
{
	int N, L, R;
	std::cin >> N >> L >> R;
	// make arr & visited
	int **arr = (int **)malloc(sizeof(int*) * N);
	int **visited = (int **)malloc(sizeof(int*) * N);
	for (int i=0; i<N; i++)
	{
		arr[i] = (int *)malloc(sizeof(int) * N);
		visited[i] = (int *)malloc(sizeof(int) * N);
		for (int j=0; j<N; j++)
		{
			std::cin >> arr[i][j];
		}
	}

	// make populations to save sum of population
	int *populations = (int *)malloc(sizeof(int) * N * N);
	int answer = 0;
	bool moved = true;
	std::queue<int> q;
	while (moved)
	{
		// set variables
		moved = false;
		int area_num = 0;
		memset(populations, 0, sizeof(int) * N * N);
		for (int i=0; i<N; i++)
		{
			memset(visited[i], 0, sizeof(int) * N);
		}
		// start BFS at not visited cell
		for (int r=0; r<N; r++)
		{
			for (int c=0; c<N; c++)
			{
				if (visited[r][c] == 0)
				{
					// start BFS
					q.push(r);
					q.push(c);
					visited[r][c] = ++area_num;
					int population_sum = 0;
					int population_count = 0;
					while (!q.empty())
					{
						int cr, cc;
						cr = q.front();
						q.pop();
						cc = q.front();
						q.pop();
						population_sum += arr[cr][cc];
						population_count += 1;
						for (int d=0; d<4; d++)
						{
							int nr, nc;
							nr = cr + dr[d];
							nc = cc + dc[d];
							if (nr < 0 || nc < 0 || N <= nr || N <= nc) continue;
							if (visited[nr][nc] != 0) continue;
							int diff = abs(arr[nr][nc] - arr[cr][cc]);
							if (diff < L || R < diff) continue;
							visited[nr][nc] = area_num;
							q.push(nr);
							q.push(nc);
						}
					}
					populations[area_num - 1] = population_sum / population_count;
				}
			}
		}
		// change population
		for (int r=0; r<N; r++) {
			for (int c=0; c<N; c++) {
				int changed_population = populations[visited[r][c] - 1];
				if (!moved && arr[r][c] - changed_population != 0) {
					moved = true;
				}
				arr[r][c] = changed_population;
			}
		}
		if (moved) answer += 1;
	}
	// print answer
	std::cout << answer;
	// for (int i=0; i<N; i++) {
	// 	for (int j=0; j<N; j++) {
	// 		std::cout << arr[i][j];
	// 	}
	// 	std::cout << '\n';
	// }
}