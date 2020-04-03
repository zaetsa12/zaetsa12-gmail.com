import random

# Exercise1

# hour = int(input('Enter hour: '))
# if hour >= 11 and hour < 16:
#     print('Good day')

# elif hour >= 5 and hour < 11:
#     print('Good morning')

# elif hour >= 16 and hour <= 21:
#     print('Good evening')

# elif hour > 21 and 0 <= hour < 5 and hour <= 24:
#     print('Good night')

# else:
#     print('Enter number from 0 to 24')

# Exercise2
# a = int(input('Виберіть дію \n 1: перевести дюйми в сантиметри \n 2: перевести сантиметри в дюйми \n'))
# b = float(input('Напишіть число '))

# if a == 1:
#     c = b*2.54
#     print(c, ' сантиметрів в', b, 'дюймах')
# elif a == 2:
#     c = b/2.54
#     print(c, ' дюймів в', b, 'сантиметрах')
# else:
#     print('Виберіть 1 або 2')


# Exercise3
# a = int(input('Виберіть дію \n 1: перевести градуси Цельсія в градуси Фарингейта \n 2: перевести градуси Фарингейта в градуси Цельсія \n'))
# b = float(input('Напишіть кількість градусів '))

# if a == 1:
#     c = b*1.8 + 32
#     print(c, ' градусів Фарингейта в', b, 'градусax Цельсія')
# elif a == 2:
#     c = (b - 32)/1.8
#     print(c, ' градусів Цельсія в', b, 'градусах Фарингейта')
# else:
#     print('Виберіть 1 або 2')

# Exercise4
# count = 0
# i = 0
# d = 1
# while i < 8:
#     i += 1
#     a = int(input( 'Введіть число \n ' ))
#     count = count + a
#     d = d * a

# print('Середнє арифметичне', count/8)
# print('Добуток', d)

# Exercise5
# t = int(input('Введіть температуру \n '))
# min = t
# max = t
# i = 0

# while i < 6:
#     i += 1
#     t = int(input('Введіть температуру \n '))
#     if t > max:
#         max = t
#     if t < min:
#         min = t

# print('Max = ', max)
# print('Min = ', min)
