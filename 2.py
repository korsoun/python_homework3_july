# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Средний элемент в списке нечетной длины возводится в квадрат

def get_pair_multiplies (num_list):
    multiple_list = []
    left_ind = 0
    right_ind = len(num_list) - 1
    while left_ind <= right_ind:
        multiple_list.append(num_list[left_ind] * num_list[right_ind])
        left_ind += 1
        right_ind -= 1
    return multiple_list

first_list = [4, 6, 3, 1, 2]
print(f'Список с парными произведениями: {get_pair_multiplies(first_list)}')
