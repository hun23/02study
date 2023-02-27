T = int(input())

for tc in range(1, T + 1):
    n, k, a, b = map(int, input().split())  # 하늘, 사진 영역, 초점 a, b(확대x)

    sky = [list(map(str, input().split())) for _ in range(n)]

    # sky에서 star의 i, j 인덱스를 각각 삽입
    star_i = []
    star_j = []
    for i in range(n):
        for j in range(n):
            if sky[i][j] == '*':
                star_i.append(i)
                star_j.append(j)

    # star의 최소, 최대 인덱스
    i_min = min(star_i)
    i_max = max(star_i)
    j_min = min(star_j)
    j_max = max(star_j)

    # while 문, cnt는 -1로 시작해 조건에 해당하지 않는 경우 그대로 -1 출력
    cnt = -1
    while True:
        # 사진 영역
        row_min = a - k // 2
        row_max = a + k // 2
        column_min = b - k // 2
        column_max = b + k // 2

        # 사진 영역 인덱스
        row_list = [x for x in range(row_min, row_max + 1)]
        column_list = [x for x in range(column_min, column_max + 1)]

        # 조건 만족하면 k+2, cnt+1 / star의 최소, 최대 인덱스는 사진영역에 있어야 함.
        if (i_min in row_list) and (i_max in row_list) and (j_min in column_list) and (j_max in column_list):  #
            k -= 2  # -2로 영역 줄이기
            cnt += 1

        else:
            break

    print(f'#{tc} {cnt}')


