# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. Пользователь в первой строке вводит натуральное число N
#  – количество элементов в списке. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите размер элементов списка: '))
list_n = input('Введите элементы списка через пробел: ').split()
arr = list(map(int, list_n))
x = int (input('Введите число х: '))
count = 0
for i in range(n):
    if arr[i] == x:
        count += 1
print(f'Число {x} встречается в списке А {count} раз.')