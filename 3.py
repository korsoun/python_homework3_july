# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части.
# Пример: [1.1 1.2 3.1 5 10.01] => 0.19

# Решение с кучей лишних знаков, дает ответ 0.5100000000000002

# import math

# def get_fract_part_difference (float_num_list):
#     max_fract = 0
#     min_fract = 1
#     for element in float_num_list:
#         mod_result = math.modf(abs(element))
#         if mod_result[0] > max_fract:
#             max_fract = mod_result[0]
#         elif mod_result[0] < min_fract:
#             min_fract = mod_result[0]
#     fract_diff = max_fract - min_fract
#     return fract_diff

# num_list = [7.78, 8.34, -1.27]
# print(get_fract_part_difference(num_list))


# Решение с нужным количеством знаков. Дает 0.7799

num_list = [7.78, 8.34, -1.27, 5.0001, 4]

def get_fract_diff (num_list):
    max_fract = 0  # Текущая максимальная дробная часть.
    min_fract = 1  # Текущая минимальная дробная часть
     
    for float_elem in num_list:
        if float_elem % 1 != 0:    # Проверка на наличие дробной части, на семинаре сказали игнорировать целые числа
            str_fract_part = ''    # Для записи цифр дробной части
            str_elem = str(float_elem) # Строковое представление числа
            point_pos = 0  # Хранит индекс точки
            for index in range(len(str_elem)):
                if str_elem[index] == '.':
                    point_pos = index
            for index in range(point_pos, len(str_elem)):  # Составление строки с дробной частью
                str_fract_part += str_elem[index]  
            float_fract_part = float(str_fract_part)
            if float_fract_part > max_fract:  # Сравнение с максимальной дробной частью
                max_fract = float_fract_part
            elif float_fract_part < min_fract: # Сравнение с минимальной дробной частью
                min_fract = float_fract_part
    fract_dif = max_fract - min_fract
    return fract_dif
print(f'Разница между наибольшей и наименьшей дробной частями: {get_fract_diff(num_list)}')







