import sys
sys.stdin = open("numcard_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))

    big_num = 0  # 제일 큰 수
    big_cnt = 0  # 제일 많은 카드
    for i in num:
        cnt = 0   # 카드 장 수
        for j in num:
            if i == j:   # 만약 중복된 카드가 있다면
                cnt += 1
        if big_cnt <= cnt and big_num < i:   # 3399 같은 경우, 3이 출력되는 예시가 존재
            big_num = i     # 따라서 현 최대숫자 < i, 현 최대 장수 < cnt 둘 다 만족시에만
            big_cnt = cnt   # 최대값에 할당해준다

    if cnt == 0:   # 중복되는 것이 없는 경우
        big_num = max(num)   # 그냥 제일 큰 숫자만 출력


    print(f'#{tc}', end = ' ')
    print(big_num, big_cnt)