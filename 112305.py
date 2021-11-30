size = input()
lst = list(map(int, input().split()))
ordered_lst = []

difference = len(lst) - len(set(lst))
for i in lst:
    if i not in ordered_lst:
        ordered_lst.append(i)

print(*(ordered_lst + [0] * difference))