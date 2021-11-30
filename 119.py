K = input()
count = 0
for i in range(1, int(K) + 1):
    if str(i) == str(i)[::-1]:
        count += 1
print(count)