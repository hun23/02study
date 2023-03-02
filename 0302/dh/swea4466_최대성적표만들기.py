T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    # 풀이1
    # scores.sort(reverse=True)
    # print(f"#{tc} {sum(scores[:K])}")

    # 풀이2, 버블소트 사용하여 직접 정렬
    for i in range(N - 1):
        for j in range(i + 1, N):
            if scores[i] < scores[j]:
                scores[i], scores[j] = scores[j], scores[i]
    # print(scores)
    print(f"#{tc} {sum(scores[:K])}")
