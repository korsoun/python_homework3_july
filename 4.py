# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def get_binary_number (number, digits):
    str_number = str(number)  # Строковое представление введенного числа
    int_part = ''  # Строковое представление целой части
    fract_part = '0.' # Строковое представление дробной части
    point_pos = -1
    for index in range(len(str_number)): # В зависимости от позиции точки раскидываем символы числа по строкам с целой и дробной части
        if str_number[index] == '.':
            point_pos = index
        if index > point_pos and point_pos == -1: # Когда не дошли до точки
            int_part += str_number[index]
        if index > point_pos and point_pos != -1: # Когда дошли до точки
            fract_part += str_number[index]
    digit_int_part = int(int_part)  # Целая часть в числовом формате
    str_binary_int = ''  # Строковое представление целой части в двоичной системе
    while digit_int_part > 0: # Переводим целую часть 
        str_binary_int += str(digit_int_part % 2)
        digit_int_part //= 2
    str_binary_int = str_binary_int[::-1] # Переворачиваем строку, чтоб получить правильный вид
    float_fract_part = float(fract_part)  # Числовой формат дробной части
    str_binary_fract = '.'  # Строковое представление дробной части в двоичном формате
    while len(str_binary_fract) < digits + 1: # Задание требуемой значности с учетом точки
        str_binary_fract += str(int(float_fract_part * 2)) # Запись целой части удвоения
        float_fract_part = float('0.' + str(float_fract_part * 2)[2:])  # Взяли дробную часть, умножили на 2, перевели в строку, получили срезом цифры после точки, составили строку вида 0.ХХХ, перевели в число
    whole_binary = float(f'{str_binary_int}{str_binary_fract}') # Результат
    return whole_binary

num = float(input('Введите число, используя точку в качестве разделителя:'))
depth = int(input('Введите количество знаков после запятой: '))
print(f'Двоичное представление числа: {get_binary_number(num, depth)}')



