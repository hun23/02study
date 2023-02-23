'''

왼쪽 아래 (x, y)
오른쪽 위(p, q)

겹치는 type
a = 3개
b = 선분으로 겹침 => same box 안의 x값이나 y값이 모두 동일해야 한다.
c = 점으로 겹침
d = 완전히 분리
'''

'''
1) 주어진 4개의 꼭지점의 관계를 파악한다.
2) l == 두 사각형의 가로, 세로 변의 길이
3) m == 두 사각형의 모든 x좌표, y좌표의 max - min 값
4) a : x, y모두 m < l이 되어야 겹친다 / d : m > l이 되어야 분리 / c,b : m==l 동일 (이외 조건 필요)
'''
for tc in range(4):
    # 1-1
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())  # input
    x = [x1, p1, x2, p2] # x 좌표 값 모으기
    y = [y1, q1, y2, q2] # y 좌표

    # 1-2 사각형의 변의 길이
    xl = (p1 - x1) + (p2 - x2)
    yl = (q1 - y1) + (q2 - y2)

    # 1-3 x, y의 최대 - 최소
    xm = max(x) - min(x)
    ym = max(y) - min(y)

    # 2
    # 조건에 따라 print
    if xm < xl and ym < yl:
        print('a')
    elif xm > xl or ym > yl:
        print('d')
    else:                       # 점으로 겹침, 선분으로 겹침의 차이 => 점으로 겹치는 모든 경우에서 else
        if (x2 == p1 and y2 == q1) or (x2 == p1 and y1 == q2) or (x1 == p2 and y1 == q2) or (x1 == p2 and y2 == q1):
            print('c')
        else:
            print('b')
