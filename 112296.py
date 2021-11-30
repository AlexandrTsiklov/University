length = int(input())
lst = list(map(int, input().split()))
max_count = 1


elem = lst[0]
count = 1
for i in range(length - 1):
    if lst[i] == lst[i + 1]:
        count += 1
    else:
        count = 1
    if count > max_count:
        max_count = count
        elem = lst[i]

print(elem, max_count)


