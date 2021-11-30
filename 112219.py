ch1, ch2 = map(int, input().split())
r, count = 0, 1

while ch1 != ch2:
    if ch1 > ch2:
        ch1 -= ch2
    else:
        ch2 -= ch1
    count += 1

print(ch2, count)
