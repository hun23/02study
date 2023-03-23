#include <iostream>

int queens[15];
int columns[15];
int d1[27];
int d2[27];

int solve(int N, int row)
{
  if (N == row) return 1;

  int ret = 0;
  for (int col = 0; col < N; col++)
  {
    // check
    if (columns[col] || d1[row + col] || d2[row + (N - col)]) continue;
    
    columns[col] = 1;
    d1[row + col] = 1;
    d2[row + (N - col)] = 1;
    ret += solve(N, row + 1);
    columns[col] = 0;
    d1[row + col] = 0;
    d2[row + (N - col)] = 0;
  }
  return ret;
}

int main(void)
{
  int N;
  std::cin >> N;

  int answer;
  answer = solve(N, 0);
  std::cout << answer;
}