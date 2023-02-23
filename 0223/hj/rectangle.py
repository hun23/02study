import sys
sys.stdin = open('input.txt', 'r')

for _ in range(4):
    lst = list(map(int, input().split()))
    maxX = max(lst[0], lst[2], lst[4], lst[6])
    minX = min(lst[0], lst[2], lst[4], lst[6])
    maxY = max(lst[1], lst[3], lst[5], lst[7])
    minY = min(lst[1], lst[3], lst[5], lst[7])

    ar = lst[2]-lst[0]
    br = lst[6]-lst[4]
    ac = lst[3]-lst[1]
    bc = lst[7]-lst[5]
    allX = ar + br
    allY = ac + bc

    if (maxX-minX) < allX and (maxY-minY) < allY:
        print('a')
    elif (maxX-minX) == allX and (maxY-minY) < allY or (maxY-minY) == allY and (maxX-minX) < allX:
        print('b')
    elif (maxX-minX) == allX and (maxY-minY) == allY:
        print('c')
    else:
        print('d')