'''
과제 제출하지 않은 사람의 번호 오름차순으로 출력
'''
T = int(input())

for tc in range(1, T + 1):
    # 1. 초기 설정
    n, k = map(int, input().split()) # 수강생 수, 과제 제출 수
    submit = list(map(int, input().split())) # 과제 제출 번호
    student = [x for x in range(1, n + 1)] # 1~n 학생 번호

    # 2
    # student 안에 없는 submit 출력
    print(f'#{tc}', end=' ')
    for i in student:
        if i not in submit:
            print(i, end=' ')
    print()