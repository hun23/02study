T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answers = []
    for r in range(N):  # row별로 먼저 찾기
        row_sum = sum(arr[r])
        filled = []
        if row_sum != 0:  # row가 비어있지 않으면
            start = -1
            end = -1
            for c in range(N):  # col별 순회
                if start == -1:  # 처음으로
                    if arr[r][c] != 0:  # 비어있지 않으면
                        start = c
                        filled.append(start)  # 채우기
                else:  
                    if arr[r][c] == 0:  # 다시 빈 것이 나타나면
                        end = c  # 끝 인덱스 저장
                        start = -1
                        filled.append(end)
                    elif c == N - 1:  # 인덱스 마지막에 도달하면
                        end = c + 1  # 끝 인덱스 저장
                        start = -1
                        filled.append(end)
            # 위 반복문이 끝나면 filled에 [start, end, start, end ... ] 저장
            for i in range(0, len(filled), 2):
                start, end = filled[i], filled[i + 1]
                ridx = 0  # row_index
                while arr[r + ridx][start] != 0:  # 사각형 0으로 만들기
                    arr[r + ridx][start:end] = [0] * (end - start)
                    ridx += 1
                    if r + ridx >= N:
                        break
                answers.append((ridx, end - start))  # 세로길이, 가로길이 저장
    answers.sort(key=lambda x: (x[0] * x[1], x[0]))  # 넓이, 세로길이 순으로 정렬
    print(f"#{tc} {len(answers)}", end=" ")
    prnt = []
    for a in answers:
        prnt.append(" ".join(map(str, a)))
    print(*prnt, sep=" ")
