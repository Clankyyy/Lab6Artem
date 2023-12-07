#1
# a = (1, 2, 3, 4)
# print(a)

#2
# a = [1, 2, 3, 4, 5, 6]
# srez = a[:3]
# print(a)
# print(srez)

# 3 (без операторов ветвления)
# a = int(input('Введите количество секунд: '))
# sec = a%60
# min = a//60%60
# hrs = a//3600
# print(str(hrs) + ' часов ' + str(min) + ' минут ' + str(sec) + ' секунд')

# 3 (с операторами ветвления)
# a = int(input('Введите количество секунд: '))
# if (a%60 == 0):
#     sec = 0
# else:
#     sec = a%60
# if a//60%60 == 0:
#     min = 0
# else:
#     min = a//60%60
# if a//3600 == 0:
#     hrs = 0
# else:
#     hrs = a//3600
# print(str(hrs) + ' часов ' + str(min) + ' минут ' + str(sec) + ' секунд')

#4
# ch1 = int(input('Введите первое число: '))
# ch2 = int(input('Введите второе число: '))
# border = max(ch1, ch2)
# for i in range(2, border):
#     if ch1 % i == 0 and ch2 % i == 0:
#         print('Наименьшее общее кратное ' + str(ch1) + ' и ' + str(ch2) + ' это ' + str(i) + '.')
#         break
# else:
#     print('Общие кратные у чисел ' + str(ch1) + ' и ' + str(ch2) + ' отсутствуют.')

#5
# def summsqrt(n):
#     summ = 0
#     for i in range(n + 1):
#         summ += (i*i)
#     return summ
#
# n = int(input('Введите число n: '))
# print(summsqrt(n))

#6
y = int(input('Введите координату ферзя по горизонтали: '))
x = int(input('Введите координату ферзя по вертикали: '))
# for x in range(1, 9):
#     for y in range(1, 9):
pole = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
print('\n')
for i in range(len(pole)):
    pole[i][y-1] = '*'
for i in range(len(pole)):
    pole[x-1][i] = '*'
temp_x = x
temp_y = y
while temp_x != 0 and temp_y >= 1:
    temp_y -= 1
    temp_x -= 1
while temp_x <= 7 and temp_y <= 7:
    pole[temp_x][temp_y] = '*'
    temp_x += 1
    temp_y += 1
    # print(temp_x, temp_y)
# pole[x - 1][y - 1] = 'Q'
# for i in range(len(pole)):
#     print(pole[i])
# print('\n')
temp_x = x - 1
temp_y = y - 1
while temp_x != 8 and temp_y >= 0:
    temp_x += 1
    temp_y -= 1
while temp_x >= 1 and temp_y <= 6:
    temp_x -= 1
    temp_y += 1
    pole[temp_x][temp_y] = '*'
    # print(temp_x, temp_y)
pole[x - 1][y - 1] = 'Q'
print('  ' + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' + '5' + ' ' + '6' + ' ' + '7' + ' ' + '8')
for i in range(len(pole)):
    print(str(i + 1) + ' ' + str(pole[i][0]) + ' ' + str(pole[i][1]) + ' ' + str(pole[i][2]) + ' ' + str(pole[i][3]) + ' ' + str(pole[i][4]) + ' ' + str(pole[i][5]) + ' ' + str(pole[i][6]) + ' ' + str(pole[i][7]))
