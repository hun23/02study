'''
1. 첫 번째 수로 양의 정수가 주어진다.
2. 두 번째 수는 양의 정수 중에서 하나를 선택한다.
3. 세 번째 부터 '앞의 앞의' 수에서 '앞의 수'를 빼서 만든다.
4. 음수 -> 버리고 더이상 x
'''
# 1
# 초기 설정
N = int(input())
cnt_lst = [] # 규칙으로 만든 수의 갯수가 들어가는 리스트
fin = [] # 만든 수들의 리스트가 들어가는 리스트

# 2
for i in range(1, N + 1):
    result = [N, i]  # 규칙에 맞는 수 채울 리스트. N과 i는 미리 넣기
    cnt = 2  # cnt는 2로 시작

    # 3
    idx = 1  # result의 idx는 1부터 시작
    while True:
        sub = result[idx - 1] - result[idx]  # 앞앞 - 앞
        if sub >= 0:
            result.append(sub)   # sub가 0이상이면 result에 더한다.
            idx += 1             # idx +
            cnt += 1             # cnt +
        else:                    # 음수가 나오면 종료.
            break
    # 4
    # while문이 종료되면, result -> fin, cnt -> cnt_lst에 넣는다.
    fin.append(result)
    cnt_lst.append(cnt)
# 5 출력
print(max(cnt_lst))
print(*fin[cnt_lst.index(max(cnt_lst))], sep=' ')