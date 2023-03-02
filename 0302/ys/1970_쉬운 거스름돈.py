'''
거슬러 주어야 할 금액 > 돈 최소 개수로 거슬러 주기
'''

T = int(input())

for tc in range(1, T + 1):
    # 1. 초기 설정
    n = int(input())
    coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    coin_cnt = [0] * 8  # coin의 수가 들어갈 리스트

    # 2
    # n을 coin[i]로 나눈 몫 -> coin_cnt / 나머지 -> n으로 갱신
    for i in range(8):
        coin_cnt[i] = n // coin[i]
        n = n % coin[i]

    print(f'#{tc}')
    print(*coin_cnt)