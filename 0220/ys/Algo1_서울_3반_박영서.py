
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    hi = [list(map(int, input().split())) for _ in range(n)]

    rlt = []
    new = [[0] * 3 for _ in range(3)]

    # 3*3 만큼 슬라이싱해서 봉우리를 찾은 후 rlt에 넣기
    # rlt가 하나 있으면 -1
    # rlt 를 sort 한 후 인덱스 사용해서 -1, -2의 차이 출력하기
    for i in range(0, n - 2):
        for j in range(0, n - 2):
            new[0] = hi[i][j : j + 3]
            new[1] = hi[i+1][j: j + 3]
            new[2] = hi[i+2][j: j + 3]

            top = new[1][1]

            for k in range(3):
                for o in range(3):
                    if new[k][o] >= top:
                        break
                    else:
                        continue
            else:
                rlt.append(top)


    # 봉우리 리스트 확인 후 출력
    if len(rlt) == 1 or len(rlt) == 0:
        print(f'#{tc} -1')

    else:
        rlt.sort()
        result = rlt[-1] - rlt[-2]
        print(f'#{tc} {result}')


