lst = input().split()
index = int(input())
lst[index:] = lst[index + 1:]
print(*lst)