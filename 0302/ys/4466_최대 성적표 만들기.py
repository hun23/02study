'''

총점이 가장 크도록 성적표 만들기
최대로 만들 수 있는 총점은 몇점인가

'''

T = int(input())

for tc in range(1, T + 1):

    n, k = map(int, input().split()) # k 과목 선택
    score = list(map(int, input().split()))

    # 내림차순 정렬, k 만큼 slicing
    score.sort(reverse=True)
    score = score[:k]

    print(f'#{tc} {sum(score)}')




