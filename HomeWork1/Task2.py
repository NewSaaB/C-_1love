# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# # Решение через "массив"
# sum_num = input("Enter your three digit number: ")
# print(int(sum_num[0]) + int(sum_num[1]) + int(sum_num[2]))

# Решение математикой
sum_num = int(input("Enter your three digit number: "))
print(f"sum of digits in a three-digit number: {(sum_num//100) + ((sum_num%100)//10) + (sum_num%10)}") # Вначале получаем 1 число, потом 2, затем 3 и складываем их
