lst = list(input().split())
position = 0
for i in range(len(lst)):
    if lst[i] != '0':
        lst[position], lst[i] = lst[i], lst[position]
        position += 1
print(*lst)





