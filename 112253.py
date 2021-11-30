# from math import sqrt
# ch = int(input())
#
# flag = 'YES'
# for i in range(2, int(sqrt(ch)) + 1):
#     if ch % i == 0:
#         flag = 'NO'
#         break
# print(flag)

N = int(input())
summa = 0
for i in range(1, N+1):
    summa += 1/(i**2)
print(summa)
