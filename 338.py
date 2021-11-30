lst = []
lst.extend(input())
for i in range(len(lst)):
    if lst[i] == '0':
        lst.pop(i)
    else:
        break

print(int(''.join(lst[::-1])))