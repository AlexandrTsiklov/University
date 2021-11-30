lst = list(map(int, input().split()))
set_lst = set(lst)
max_count, count, elem = 0, 0, 0
for i in set_lst:
    if lst.count(i) >= max_count:
        max_count = lst.count(i)
        elem = i
print(elem)
