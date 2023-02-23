from sys import stdin

c, r = map(int, stdin.readline().split())
N = int(input())

x = y = cnt = pivot = 1

if N == 1:
    print(x, y)
elif N > r * c:
    print(0)
else:
    done = False
    while True:

        while y != r:
            y += 1
            cnt += 1
            if cnt == N:
                print(x, y)
                done = True
                break

        if done:
            break

        while x != c:
            x += 1
            cnt += 1
            if cnt == N:
                print(x, y)
                done = True
                break

        if done:
            break

        while y != pivot:
            y -= 1
            cnt += 1
            if cnt == N:
                print(x, y)
                done = True
                break

        if done:
            break

        while x != pivot+1:
            x -= 1
            cnt += 1
            if cnt == N:
                print(x, y)
                done = True
                break

        if done:
            break

        r -= 1
        c -= 1
        pivot += 1