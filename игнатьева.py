#1
user_num = input('Задание 1. Введите целое число: ')

#проверка на наличие каких-либо символов помимо цифр 0-9
try:
    user_num = int(user_num)
    print('Тип данных: ', type(user_num))

    user_num = str(user_num)
    print('Тип данных: ', type(user_num))

except ValueError:  #если пользователь ввел что-то помимо цифр, выводится предупреждение
    print('используйте только цифры 0-9')

#2
user_num = input('Задание 2. введите положительное или отрицательное число: ')

#опять проверка на ненужные символы
try:
    user_num = int(user_num)
    if user_num < 0:
        print(user_num)
    else:
        print(-user_num)

except ValueError:
    print('используйте только цифры 0-9')

#3
cap = int(input(' Задание 3. введите вместимость автобуса: '))
on = int(input('введите кол-во пассажиров в автобусе: '))
wait = int(input('введите кол-во ожидающих автобус '))
losers = cap - on - wait    #оставшиеся ждать люди
if losers <= 0: #если остались люди без мест, выводим их количество
    print('осталось ждать: ', -losers)
else:
    print('все поместились в автобус!')

#4
user_name = input('Задание 4. введите своё имя: ')
print('Здравствуйте,', user_name, '!')

#5
user_num1 = input('Задание 5. введите целое число: ')
user_num2 = input('введите второе целое число: ')

#проверка но то точно ли пользователь ввел числа
try:
    user_num1 = int(user_num1)
    user_num2 = int(user_num2)
    print(user_num1 * user_num2)
except ValueError:
    print('используйте цифры 0-9')