# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def get_sum_of_odds (num_list):
    result = 0
    index = 1
    while index < len(num_list):
        result += num_list[index]
        index += 2
    return result

some_list = [2, 9, 8, 3, 4]
print(f'Сумма элементов списка на нечетных позициях рана: {get_sum_of_odds(some_list)}')