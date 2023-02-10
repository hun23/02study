N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = []

sum = 0
prefix_sum = [0]

for i in lst:
    sum += i
    prefix_sum.append(sum) # 누적합

l = list(range(0, N-K+1))
r = list(range(K, N+1))

for left, right in zip(l, r):
    ans.append(prefix_sum[right]-prefix_sum[left])

print(max(ans)) # 데이터 값이 모두 0 이하면 오류가 있었는데... 인덱스 범위 지정 실수였습니다 ٩( ᐛ )و