#1
# создаем переменные employed и vacation по умолчанию принимающие значение False (будто пользователь не трудоустроен)
employed = False
vacation = False

#вопросы для пользователя q = question
q1 = input('1. вы трудоустроены?: ')
q2 = input('вы в отпуске?: ')

if q1 == 'да':
    if q2 == 'да':
        vacation = True
    else:
        employed = True

# проверяем ответы пользователя и выводим ответ в соответсвии с ними
if vacation:
    print('вам не нужно ставить будильник на утро! хорошего отдыха')
elif employed:
    print('вам нужно поставить будильник на утро. не опоздайте на работу, удачи!')

#2
operation = input('2. введите знак математической операции: ')
value_1 = int(input('введите первое целое число: '))
value_2 = int(input('введите второе целое число: '))
#выводим результат в соответствии с знаком который ввел пользователь
if operation == '-':
    print(value_1 - value_2)
elif operation == '+':
    print(value_1 + value_2)
elif operation == '*':
    print(value_1 * value_2)
elif operation == '/':
    print(value_1 / value_2)

#3
user_num1 = int(input('3. введите первое целое число: '))
user_num2 = int(input('введите второе целое число: '))
summa = 0
for x in range(user_num1, user_num2 + 1):
    summa += x
print('сумма чисел в заданном промежутке:', summa)

#4
month = int(input('4. введите номер месяца: '))
if 0 < month < 13:  #на всякий случай, если пользователь ошибся
    quarter = month // 4 + 1    #1-3 месяц считались бы 0 кварталом, нужно прибавить 1
    print('квартал:', quarter)
if month == 12 or month == 1 or month == 2:
    print('сезон: зима')
elif month == 3 or month == 4 or month == 5:
    print('сезон: весна')
elif month == 6 or month == 7 or month == 8:
    print('сезон: лето')
else:
    print('сезон: осень')

#5
print('5. для остановки программы нужно ввести число -1')
marks = 0
count = 0
while True:  #пользователь вводит оценки, пока не остановит программу
    user_mark = int(input('введите оценку: '))
    if user_mark == -1:     #проверяем не равно ли число -1, чтобы не прибавлять к нашим значениям
        break
    marks += user_mark
    count += 1

sr_mark = marks / count
print('средний балл:', sr_mark)

if sr_mark >= 90:   #выводим оценку
    print('A')
elif sr_mark >= 80:
    print('B')
elif sr_mark >= 70:
    print('C')
elif sr_mark >= 60:
    print('D')
elif sr_mark < 60:
    print('F')
