students_dict = {}
print('Формат: Фамилия Имя БалФизика БаллИстория БаллРусский')
student = list(input().split())

m = -1
while student:
    students_dict[student[0] + ' ' + student[1]] = (int(student[2]), int(student[3]), int(student[4]))
    sm = sum(map(int, (student[2], student[3], student[4])))
    if sm > m:
        m = sm
    student = list(input().split())

print('Всего участников:', len(students_dict))
for student in students_dict:
    if sum(students_dict[student]) == m:
        print(student, 'набрал', m, 'баллов - это максимум')

