# Состаить список чисел Фибоначчи с отрицательными числами
# Для k=8 [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def get_full_Fibonacci (k):
    fib_pos_list = []  # хранит список с положительным рядом
    fib_neg_list_inv = [] # хранит список с отрицательным рядом в обратном порядке
    for i in range(k):  # правила для заполнения списков
        if i == 0:
            fib_pos_list.append(1)
            fib_neg_list_inv.append(1)
        if i == 1:
            fib_pos_list.append(1)
            fib_neg_list_inv.append(-1)
        if i > 1:
            fib_pos_list.append(fib_pos_list[len(fib_pos_list)-2] + fib_pos_list[len(fib_pos_list)-1])
            fib_neg_list_inv.append(fib_neg_list_inv[len(fib_neg_list_inv)-2] - fib_neg_list_inv[len(fib_neg_list_inv)-1])
    fib_full_list = []  # хранит весь список
    i = k-1
    while i >= 0:
        fib_full_list.append(fib_neg_list_inv[i])  # заполнение отрицательным рядом
        i -= 1
    fib_full_list.append(0)  # добавление нуля
    for i in range(k):
        fib_full_list.append(fib_pos_list[i])   # заполнение положительным рядом
    return fib_full_list

k = int(input('Введите число k: '))
print(get_full_Fibonacci(k))
        