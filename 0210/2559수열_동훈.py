N, K = map(int, input().split())
arr = list(map(int, input().split()))
s = sum(arr[0 : 0 + K])  # 처음(인덱스=0) K 까지의 합
mx = s  # 최대값을 처음값으로 초기화
for i in range(1, N - K + 1):  # 인덱스 1부터 N - K 까지
    # 이전 인덱스의 값(arr[i-1])을 빼고 다음 인덱스의 값(arr[i-1 + K]) 더하기
    s = s - arr[i - 1] + arr[i - 1 + K]
    if s > mx:
        mx = s
print(mx)
