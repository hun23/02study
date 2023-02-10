'''

100*100 정사각형 도화지

10*10 검은색 색종이 => 여러장 붙인 후 색종이가 붙은 검은 영역의 넓이 구하라

'''

import sys
input = sys.stdin.readline

arr = [[0]*100 for _ in range(100)] # 100*100

num = int(input())
cnt = 0
# 1
# 검은색 색종이의 범위만큼 arr에 1추가, cnt +1 한다.
# 다음 색종이가 왔을 때, 1이 있다면 cnt +1 하지 않도록 if문 활용
for k in range(num):

    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
print(cnt)


















