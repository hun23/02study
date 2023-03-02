import sys
sys.stdin = open("coloring_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    purple = 0
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                arr[i][j] += color
                if arr[i][j] == 3:
                    purple += 1

    print(f'#{tc} {purple}')