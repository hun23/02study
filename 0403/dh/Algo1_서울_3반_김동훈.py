T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = int(input(), 16)          # 16진법 string -> 10진법 int

    cnt, answer, i = 0, 0, 0        # cnt 에 연속된 1의 개수 저장, answer 에 최대값 저장
    while (1 << i) <= num:          # num 의 2진법 자릿수를 확인
        if num & (1 << i):          # 1인 경우
            cnt += 1                # cnt 추가
            if cnt > answer:        # cnt > answer 이면 answer 갱신
                answer = cnt
                if answer == 9:     # 1은 최대 9개 까지 연속할 수 있으므로
                    break
        else:
            cnt = 0                 # 0인 경우 cnt 초기화
        i += 1
    print(f"#{tc} {answer}")

# 1번
# def to_bin(num, depth):
#     if depth == 0:  # 자릿수 채우기 위해 4번 반복
#         return ""
#     quo, rem = divmod(num, 2)
#     return to_bin(quo, depth - 1) + str(rem)
#
#
# def solve(h, depth):
#     if depth == 0:  # 자릿수 채우기 위해 N번 반복
#         return ""
#     ret = to_bin(int(h[0], 16), 4)  # 16진수 -> 4자리 2진수
#     return ret + solve(h[1:], depth - 1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     inp = list(input())
#     line = solve(inp, N)  # 16진법 -> N*4만큼 자릿수 채운 2진법
#     # print(line)
#     # temp 변수에 연속된 1의 개수 저장, answer 변수에 그 중 최대값 저장
#     temp, answer = 0, 0
#     for c in line:
#         if c == "0":
#             temp = 0  # 0인 경우 초기화
#             continue
#         # 1인 경우
#         temp += 1
#         if temp > answer:  # 최대값인 경우 answer 갱신
#             answer = temp
#             if answer == 9:  # 1은 최대 9개까지 연속할 수 있으므로
#                 break
#     print(f"#{tc} {answer}")

# 2번
# def to_bin(num, depth):
#     if depth == 0:  # 자릿수 채우기 위해 4번 반복
#         return ""
#     quo, rem = divmod(num, 2)
#     return to_bin(quo, depth - 1) + str(rem)
#
#
# def solve(hexx, depth, cnt, answer):  # cnt 에 연속되는 1 개수 저장, answer 에 최대값 저장
#     if depth == 0:  # 자릿수 채우기 위해 N번 반복
#         return answer
#     ret = to_bin(int(hexx[0], 16), 4)  # 16진수 -> 4자리 2진수
#     for c in ret:
#         if c == "0":                # 0이면
#             cnt = 0                 # cnt 초기화
#             continue
#         cnt += 1
#         answer = max(answer, cnt)   # 1인 경우 +1 후 answer 갱신
#         if answer == 9:
#             return 9                # 1은 최대 9개까지 연속할 수 있으므로
#     return solve(hexx[1:], depth - 1, cnt, answer)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     inp = list(input())
#     print(f"#{tc} {solve(inp, N, 0, 0)}")
