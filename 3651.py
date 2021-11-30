lst = []
start = 1

while start != 0:
    start = int(input())
    if start != 0:
        lst.append(start)

print(sum(lst)/len(lst))
