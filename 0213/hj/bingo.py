# bingo = [list(map(int, input().split())) for _ in range(5)] # 철수 빙고판
# mic = [list(map(int, input().split())) for _ in range(5)] # 사회자 빙고판

bingo = [[11, 12, 2, 24, 10], [16, 1, 13, 3, 25], [6, 20, 5, 21, 17], [19, 4, 8, 14, 9], [22, 15, 7, 23, 18]]
mic = [[5, 10, 7, 16, 2], [4, 22, 8, 17, 13], [3, 18, 1, 6, 25], [12, 19, 23, 14, 21], [11, 24, 9, 20, 15]]

for i in range(5):
    for j in range(5):
        ans = i+j+1
        for k in range(5):
            if ans in bingo[k]: # 사회자가 부른 번호가 배열 k번째 리스트 원소에 있다면
                bingo[k][bingo[k].index(ans)] = 0 # 해당 번호를 0으로 바꾸기
                cnt = 0
                r = 0
                c = 0

                for r in range(5):
                    temp = []
                    temp += bingo[r]
                    if temp == [0, 0, 0, 0, 0]:
                        cnt += 1
                        if cnt == 3:
                            print(ans)

                for r in range(5):
                    temp = []
                    for c in range(5):
                        temp.append(bingo[c][r])
                    if temp == [0, 0, 0, 0, 0]:
                        cnt += 1
                        if cnt == 3:
                            print(ans)

                temp = []
                for s in range(5):
                    temp.append(bingo[s][s])
                if temp == [0, 0, 0, 0, 0]:
                    cnt += 1
                    if cnt == 3:
                        print(ans)

                temp = []
                for s in range(4, -1, -1):
                    temp.append(bingo[s][4-s])
                if temp == [0, 0, 0, 0, 0]:
                    cnt += 1
                    if cnt == 3:
                        print(ans)