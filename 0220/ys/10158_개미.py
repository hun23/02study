'''
가로 w, 세로 h인 2차원 격자 공간
(0, 0)
개미는 (p, q), 한시간 후에 (p+1, q + 1)로 옮겨 간다.
경계면에 부딪치면 같은 속력으로 반사되어 움직인다.
t 시간 후의 위치(x, y)계산하여 출력

6 4
4 1
8


'''

w, h = map(int, input().split())

arr = [[0] * h for _ in range(w)]
p, q = map(int, input().split())

def down(p, q):  # 대각선 내려가기
    global c
    global t
    while c < t:
        if p == 0 and q == 0:
            arr[p][q] = arr[p + 1][q + 1]
            c += 1
            break

        else:
            while p < h and q < w:
                arr[p][q] = arr[p - 1][q - 1]
                c += 1
    return p, q

def up(p, q):  # 대각선 올라가기
    global c
    global t
    while c < t:
        if p == h and q == w:
            arr[p][q] = arr[p - 1][q - 1]
            c += 1
            break

        else:
            while p < h and q < w:
                arr[p][q] = arr[p + 1][q + 1]
                c += 1
    return p, q

t = int(input())
c = 0
while c < t:
    if p == h and q == w:
        arr[p][q] = arr[p - 1][q - 1]
        c += 1
        down(p, q)

    elif p == 0 and q == 0:
        arr[p][q] = arr[p + 1][q + 1]
        c += 1
        up(p, q)

    elif p == h and q != w:
        arr[p][q] = arr[p - 1][q + 1]
        c += 1
        down(p, q)

    elif p != h and q == w:
        arr[p][q] = arr[p - 1][q + 1]
        c += 1
        up(p, q)

    else:
        up(p, q)

print(p, q)


