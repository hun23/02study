'''
0~9, N개의 숫자가 나열된 수열
1. 연속해서 커지거나
2. 연속해서 작아지는 수열 중 가장 길이가 긴 것 찾아 그 길이 출력(같은 것 포함)
'''
import sys
input = sys.stdin.readline

# 1
N = int(input())
nums = list(map(int, input().split()))
cnt_lst = [] # if문이 종료됐을때 그때의 cnt가 채워지는 리스트
cnt = 0

for i in range(N - 1):
    # 2-1 작다면
    if nums[i] < nums[i + 1]:
        cnt += 1  # 횟수 +1
        i += 1  # 인덱스 이동
        while True:
            if i < N - 1 and nums[i] <= nums[i + 1]:  # 계속 작거나 같아야 한다
                cnt += 1
                i += 1
            else:
                cnt_lst.append(cnt)
                cnt = 0  # cnt 초기화
                break
    # 2-2 크다면
    elif nums[i] > nums[i + 1]:
        cnt += 1
        i += 1
        while True:
            if i < N - 1 and nums[i + 1] <= nums[i]:  # 계속 크거나 같아야 한다
                cnt += 1
                i += 1
            else:
                cnt_lst.append(cnt)
                cnt = 0
                break
    # 2-3. 같다면 +1
    else:
        cnt += 1

# 3. 마지막 cnt 리스트에 더하기
cnt_lst.append(cnt)
print(max(cnt_lst) + 1)  # 최댓값 + 1(자기자신) 출력