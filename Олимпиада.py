students_dict = {}
student = list(input().split())
s = {'Физика', 'История', 'Русский'}
people = {}

while student:
    number = 1
    name, surname = student[0], student[1]
    if (name + ' ' + surname) not in students_dict:
        students_dict[name + ' ' + surname] = {}
    students_dict[name + ' ' + surname]['id'] = f'{str(number)}_{surname[0]}_{len(name)}'
    j = 2
    for i in s:
        try:
            students_dict[name + ' ' + surname][i] = student[j]
        except:
            students_dict[name + ' ' + surname][i] = 'не учавствовал'
        j += 1
    number += 1
    student = list(input().split())

m = -1
for student in students_dict:
    sm = 0
    for param in students_dict[student]:
        if students_dict[student][param].isdigit():
            sm += int(students_dict[student][param])
    people[student] = sm
    if sm > m:
        m = sm


for s in people:
    if people[s] == m:
        print('----------------------------------------------')
        print(s, 'набрал максимум -', m)
        print('id:', students_dict[s]['id'])
        print('Физика:', students_dict[s]['Физика'])
        print('Русский:', students_dict[s]['Русский'])
        print('История:', students_dict[s]['История'])
        print('----------------------------------------------')

