w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

new_p = (p + t) % (2 * w)
new_q = (q + t) % (2 * h)

if new_p > w:
    new_p = 2 * w - new_p

if new_q > h:
    new_q = 2 * h - new_q

print(new_p, new_q)
