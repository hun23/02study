def change_status(arr, idx):
    arr[idx] = 1 if arr[idx] == 0 else 0


n = int(input())
arr = [-1] + list(map(int, input().split()))  # 0번 스위치 따로 추가
student_num = int(input())
student_arr = []
for _ in range(student_num):
    student_arr.append(tuple(map(int, input().split())))
# 입력된 학생 순서로 순회
for (s, num) in student_arr:
    if s == 1:  # 남학생
        for multi in range(num, n + 1, num):  # num의 배수
            change_status(arr, multi)
    else:  # 여학생
        arr[num] = 1 if arr[num] == 0 else 0  # 해당 칸 일단 바꾸기
        left = num
        right = num
        while True:
            # 왼쪽 오른쪽으로 한칸씩 옮겨가며
            left = left - 1
            right = right + 1
            if 0 < left and right <= n:  # 인덱스 범위 내에서
                if arr[left] == arr[right]:  # 두 스위치 상태가 같으면
                    change_status(arr, left)  # 바꾸기
                    change_status(arr, right)
                else:
                    break
            else:
                break
for (i, status) in enumerate(arr[1:]):  # 1번 스위치부터
    print(status, end=("\n" if i % 20 == 19 else " "))  # 출력
