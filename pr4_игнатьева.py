#1
def f(operation, value_1, value_2):
    if operation == '-':
        return value_1 - value_2
    elif operation == '+':
        return value_1 + value_2
    elif operation == '*':
        return value_1 * value_2
    elif operation == '/':
        return value_1 / value_2

o = input('1. введите знак математической операции: ')
a = int(input('введите первое целое число: '))
b = int(input('введите второе целое число: '))
result = f(o, a, b)
print('Результат:', result)

#1.2

def f(month):
    if 0 < month < 13:
        quarter = month// 4 + 1     #формула (month - 1)//3 + 1 неправильно выводила кварталы, поэтому оставила эту
    if month == 12 or month == 1 or month == 2:
        season = 'зима'
    elif month == 3 or month == 4 or month == 5:
        season = 'весна'
    elif month == 6 or month == 7 or month == 8:
        season = 'лето'
    else:
        season = 'осень'

    return f"квартал: {quarter}, Сезон: {season}"

m = int(input('1.2. введите номер месяца: '))
result = f(m)
print(result)

#2
def count_symbols(string):
    result = {}
    for symbol in string:
        if symbol in result:
            result[symbol] += 1
        else:
            result[symbol] = 1

    return result

s = input('2. введите предложение: ')
result = count_symbols(s)
print(result)


#3
def count_m_to_z(string):
    count = 0
    for letter in string:
        if 'm' <= letter <= 'z':
            count += 1

    return count

s = input('3. введите строку состоящую только из букв a-z: ')
result = count_m_to_z(s)
print(result)