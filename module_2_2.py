first=int(input('Ввод 1 :'))
second=int(input('Ввод 2:'))
third=int(input('Ввод 3:'))
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')