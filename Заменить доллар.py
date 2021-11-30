s = input()
ind, s1 = s.find('$'), s.replace('$', 'S')
if s1 != -1:
    print('Введённая строка идеальна')
else:
    print(s1)
    print(ind)