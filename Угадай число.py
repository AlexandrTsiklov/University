from random import randint
#1
lst1 = [i for i in range(1, 11)]
print(lst1)

#2
lst2 = [i for i in range(1, int(input()) + 1)]
print(lst2)

#3
lst3 = [i for i in range(2, 17, 2)]
print(lst3)

#4
lst4 = [i for i in range(19, -1, -1)]
print(lst4)

#5
lst5 = [randint(100, 1000) for i in range(10)]
print(lst5)

#6
lst6 = ['p', 'y', 't', 'h', 'o', 'n']
print(lst6)

#7
lst7 = list(input())
print(lst7)

#8
lst8 = [randint(-10, 11) for i in range(20)]
print(lst8)
sm = sum(lst8)
print(sm)
count_above_zero = len(list(filter(lambda x: x > 0, lst8)))
print(count_above_zero)
sum_below_zero = sum(list(filter(lambda x: x < 0, lst8)))
print(sum_below_zero)

#9
lst9 = [randint(0, 11) for i in range(10)]
count = 0
for i in range(len(lst9)):
    if lst9[i] == i:
        count += 1
print(count)



