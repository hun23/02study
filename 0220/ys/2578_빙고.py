
arr = [list(map(int, input().split())) for _ in range(5)]  # 내 배열
solution = [list(map(int, input().split())) for _ in range(5)]  # 사회자의 배열 > 한줄로 만들기
sol = sum(solution, [])

# 1
# 사회자가 부른 수를 arr에서 찾고, 그 인덱스 i, j를 row와 colum의 동일한 인덱스에 +1 해준다.
row = [0] * 5
column = [0] * 5
dia = [0] * 2 # 대각선은 2가지 경우/ i = j, dia_lst에 있는 경우
dia_lst = [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]
cnt = 0

# 2-1
# 1) sol을 전체 for문으로 돌린다.
# 2) sol[s]와 같은 값을 arr에서 찾고, 그 인덱스를 row, column, dia에 더한다.
# 3) row, column, dia에 5가 생긴다면, cnt +1을 하고 0으로 갱신한다. => cnt가 3이상이 되면 break
for s in range(25):
    if cnt >= 3:  # cnt가 3이상, break
        break
    else:
        for i in range(5):
            for j in range(5):
                if sol[s] == arr[i][j]:
                    # 2-2 인덱스 추가
                    row[i] += 1
                    column[j] += 1
                    if i == j:
                        dia[0] += 1

                    if [i, j] in dia_lst:
                        dia[1] += 1

                    # 2-3 row, column, dia에 5가 있는지 확인 => cnt+1, 0으로 갱신
                    if 5 in row:
                        cnt += 1
                        row[row.index(5)] = 0

                    if 5 in column:
                        cnt += 1
                        column[column.index(5)] = 0

                    if dia[0] == 5:  # dia는 가운데 수가 채워질 때 동시에 빙고가 될 가능성이 있으므로 따로 cnt
                        cnt += 1
                        dia[0] = 0

                    if dia[1] == 5:
                        cnt += 1
                        dia[1] = 0

print(s)















