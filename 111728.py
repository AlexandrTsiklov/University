N, K = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))


# Определяет является ли элемент крайним слева
def we_need_left_search(ind, elem):
    return not(ind == 0 or lst1[ind - 1] < elem)


# Определяет является ли элемент крайним справа
def we_need_right_search(ind, elem):
    return not(ind == len(lst1) - 1 or lst1[ind + 1] > elem)


# Возвращает индекс найденного элемента
def bin_search(lst, elem):
    left = 0
    right = len(lst)

    while True:
        middle = (left + right) // 2

        if right == left and elem != lst[0]:
            return 0, 0

        if elem < lst[middle]:
            right = middle
        elif elem > lst[middle]:
            left = middle + 1
        else:
            return middle, True


# Левый бинарный поиск
def l_bin_search(right, elem):
    left = 0

    if we_need_left_search(right, elem):
        while True:
            middle = (right + left) // 2
            if lst1[middle] != elem:
                left = middle + 1
            else:
                right = middle
                if we_need_left_search(middle, elem):
                    continue
                else:
                    return middle
    else:
        return right


# Правый бинарный поиск
def r_bin_search(left, elem):
    right = len(lst1) - 1

    if we_need_right_search(left, elem):
        while True:
            middle = (right + left) // 2
            if lst1[middle] != elem:
                right = middle
            else:
                left = middle + 1
                if we_need_right_search(middle, elem):
                    continue
                else:
                    return middle
    else:
        return left


# ind - индекс найденного бинарным поиском элемента
for i in lst2:
    ind, flag = bin_search(lst1, i)
    if flag is True:
        print(l_bin_search(ind, i) + 1, r_bin_search(ind, i) + 1, sep=' ')
    else:
        print(ind)

