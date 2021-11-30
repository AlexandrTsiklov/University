N, K = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

# Бинарный поиск через рекурсию
# def split_list(lst, ch):
#
#     if ch == lst[0]:
#         return 'YES'
#     elif len(lst) == 1:
#         return 'NO'
#
#     average = lst[len(lst) // 2]
#     if ch < average:
#         return split_list(lst[:len(lst) // 2], ch)
#     else:
#         return split_list(lst[len(lst) // 2:], ch)
#
#
# for i in lst2:
#     print(split_list(lst1, i))


def bin_search(lst, elem):
    left = 0
    flag = 'NO'
    right = len(lst)

    while True:
        middle = (left + right) // 2

        if right == left and elem != lst[0]:
            break

        if elem < lst[middle]:
            right = middle
        elif elem > lst[middle]:
            left = middle + 1
        else:
            flag = 'YES'
            break

    return flag


for i in lst2:
    print(bin_search(lst1, i))
