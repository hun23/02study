# https://www.acmicpc.net/problem/11866

N, K = map(int, input().split())
q = [_ for _ in range(1, N + 1)]  # 리스트 컴프리핸션

lst = []  # 제거된 인덱스 리스트
remove = 0  # 제거한 인덱스
while len(q) > 0:
    remove += K - 1
    if remove >= len(q):
       remove = remove % len(q)   # 한바꾸 돌았으니까 나머지를 remove에 할당
    lst.append(q.pop(remove))

    ans = str(lst)[1:-1]  # 자꾸 리스트 형태로 출력되서 구글링함.
    # 보아하니 lst 대괄호 까지 str 취급해서 앞 뒤 자르고 출력하는듯.
print(f'<{ans}>')