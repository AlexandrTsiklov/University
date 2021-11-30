# ch = int(input())
# summa = 0
# del_list = []
#
# for i in range(1, int(ch/2) + 1):
#     if ch % i == 0:
#         summa += i
#         del_list.append(i)
#
# if summa == ch:
#     print(*del_list)
# else:
#     print(0)

ch = int(input())
s = [j for j in range(1, ch // 2 + 1) if not ch % j]
if sum(s) == ch:
    print(*s)
else:
    print(0)
