ch1, ch2 = map(int, input().split())
count, r, m, n = 0, 0, max(ch1, ch2), min(ch1, ch2)
while n != 0:
    r = m % n
    m = n
    n = r
    count += 1
print(m, count)
