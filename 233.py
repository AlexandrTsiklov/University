length = int(input())
arr = list(map(int, input().split()))


def bubble_sort(our_arr):
    flag = True
    while flag:
        flag = False
        for i in range(len(our_arr) - 1):
            if our_arr[i] > our_arr[i + 1]:
                our_arr[i], our_arr[i + 1] = our_arr[i + 1], our_arr[i]
                flag = True


bubble_sort(arr)
print(*arr)