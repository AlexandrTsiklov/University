import random


l = 10
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
for i in range(0, len(a)-1):
    for j in range(0, len(a)-1):
        s += 1
        if a[j] > a[j+1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Частично сортированный пузырёк из", l)
a = []
for i in range(0,l):
    a.append(random.randint(0,1000))
print(a)

s = 0
p = 0
for i in range(0, len(a)-1):
    for j in range(0, len(a)-1):
        s += 1
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Пузырьком из", l)
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):
        s += 1
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Вставками несортированный список из",l)
a = []
for i in range(0, l):
    a.append(random.randint(0,1000))
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            p += 1
        else:
            break
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Вставками частично из",l)
a = []
for i in range(0, l):
    a.append(random.randint(0,1000))
print(a)
for j in range(0, (len(a)//2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j+1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j-1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            p += 1
        else:
            break
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Вставками сортированный список из",l)
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j - 1], a[j]
            p += 1
        else:
            break
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Выбором несортированный список из",l,"элементов")
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
for i in range(0, len(a)):
    minim = i
    for j in range(i + 1, len(a)):
        s += 1
        if a[j] < a[minim]:
            minim = j
    a[minim], a[i] = a[i], a[minim]
    p += 1
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Выбором частично сортированный список из",l,"элементов")
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
for j in range(0, (len(a) // 2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
for i in range(0, len(a)):
    minim = i
    for j in range(i +1, len(a)):
        s += 1
        if a[j] < a[minim]:
            minim = j
    a[minim], a[i] = a[i], a[minim]
    p += 1
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print(" Выбором сортированный список из",l)
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s=0
p=0
for i in range(0, len(a)):
    minim = i
    for j in range(i + 1, len(a)):
        s += 1
        if a[j] < a[minim]:
            minim = j
    a[minim], a[i] = a[i], a[minim]
    p += 1
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Шелла несортированный список из",l)
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
diap = len(a) // 2
while diap > 0:
    for i in range(diap, len(a)):
        cur = a[i]
        pos = i
        while pos >= diap and a[pos-diap] > cur:
            s += 1
            p += 1
            a[pos] = a[pos-diap]
            pos -= diap
            a[pos] = cur
    diap = diap//2
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Шелла частично сортированный список из",l)
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
for j in range(0, (len(a) // 2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
diap = len(a) // 2
while diap > 0:
    for i in range(diap, len(a)):
        cur = a[i]
        pos = i
        while pos >= diap and a[pos-diap] > cur:
            s += 1
            p += 1
            a[pos] = a[pos - diap]
            pos -= diap
            a[pos] = cur
    diap = diap // 2
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


print("Шелла сортированный список из",l)
a = []
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
diap = len(a) // 2
while diap > 0:
    for i in range(diap, len(a)):
        cur = a[i]
        pos = i
        while pos >= diap and a[pos-diap] > cur:
            s += 1
            p += 1
            a[pos] = a[pos-diap]
            pos -= diap
            a[pos] = cur
    diap = diap // 2
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("-----------------------------------------------------------------------")


def test(arr):
    global c_comp, c_swap
    c_comp, c_swap=0, 0
    quick_sort(arr, 0, len(arr)-1)


def quick_sort(x, ibeg, iend):
    global c_comp, c_swap
    if (iend - ibeg) <= 1:
        return
    isep = (ibeg+iend) // 2
    sep = x[isep]
    i = ibeg
    j = iend
    while True:
        while x[i] < sep:
            i += 1
            c_comp += 1
        while x[j] > sep:
            j -= 1
            c_comp += 1
        if i <= j:
            x[i], x[j] = x[j], x[i]
            c_swap += 1
            i += 1
            j -= 1
        if i >= j:
            break
    quick_sort(x,ibeg,j)
    quick_sort(x,i,iend)


print("QSort несортированный список из",l)
x = []

for i in range(0, l):
    x.append(random.randint(0, 1000))
print(x)
test(x)
print(x)
print('Сравнения - '+str(c_comp))
print('Перестановки - '+str(c_swap))


print("QSort частично сортированный список из",l)
x = []
for i in range(0, l):
    x.append(random.randint(0, 1000))
print(x)
for j in range(0, len(x) // 2):
    for j in range(0, len(x)//2):
        if x[j] > x[j + 1]:
            x[j + 1], x[j] = x[j], x[j + 1]
print(x)
test(x)
print(x)
print('Сравнения - '+str(c_comp))
print('Перестановки - '+str(c_swap))
print("-----------------------------------------------------------------------")


print("QSort ортированный список из",l)
x = []
for i in range(0, l):
    x.append(random.randint(0, 1000))
print(x)
x.sort()
print(x)
test(x)
print(x)
print('Сравнения - '+str(c_comp))
print('Перестановки - '+str(c_swap))


