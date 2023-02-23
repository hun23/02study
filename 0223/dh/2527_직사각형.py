def get_code(xlen, axlen, bxlen):
    """
    xlen => 두 사각형을 감싸는 사각형의 x변 길이
    axlen, bxlen => a, b 사각형의 x변 길이
    """
    if xlen > axlen + bxlen:
        return 1
    elif xlen < axlen + bxlen:
        return -1
    else:
        return 0


for _ in range(4):
    inp = list(map(int, input().split()))  # 입력
    ax1, ay1, ax2, ay2 = inp[:4]
    bx1, by1, bx2, by2 = inp[4:]

    # 각 변의 길이
    axlen = ax2 - ax1
    aylen = ay2 - ay1
    bxlen = bx2 - bx1
    bylen = by2 - by1

    minx = 50001
    miny = 50001
    maxx = -1
    maxy = -1
    for i in range(0, 8, 2):  # X좌표 비교
        if inp[i] > maxx:
            maxx = inp[i]
        if inp[i] < minx:
            minx = inp[i]
    for j in range(1, 8, 2):  # Y좌표 비교
        if inp[j] > maxy:
            maxy = inp[j]
        if inp[j] < miny:
            miny = inp[j]
    # xlen, ylen => 두 사각형을 감싸는 큰 사각형의 x, y변 길이
    xlen = maxx - minx
    ylen = maxy - miny
    # 큰 사각형 변의 길이와 각 사각형 변 길이 합의 관계를 반환
    xcode = get_code(xlen, axlen, bxlen)
    ycode = get_code(ylen, aylen, bylen)
    # 경우의 수 계산
    if xcode == 0 and ycode == 0:
        print("c")
    elif xcode + ycode >= 0:
        print("d")
    elif xcode + ycode == -1:
        print("b")
    else:
        print("a")
