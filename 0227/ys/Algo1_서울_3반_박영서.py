T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())  # 행, 열

    garden = [list(map(int, input().split())) for _ in range(n)]
    tree = [] # 심어지는 나무 저장할 lst

    for j in range(0, m, 2): # 두칸씩 뛰면서 저장
        for i in range(n):
            tree.append(garden[i][j])

    # 값 구하기
    cost = sum(tree)
    nums = len(tree)
    high = max(tree)

    # 가장 비싼 나무의 인덱스 구하기
    idx = []
    for i in range(len(tree)):
        if tree[i] == high:
            idx.append(i)

    high_column = divmod(idx[-1], n)  # tree리스트에서의 인덱스를 n으로 나눈 몫에 곱하기 2를 하고 +1을 하면 열의 위치가 된다.

    print(f'#{tc} {cost} {nums} {high} {high_column[0] * 2 + 1}')






