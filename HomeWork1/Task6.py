# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# Решение математикой
num = int(input("Enter your number ticket: "))
sum_end = int((num//100)%10 + ((num//10)%10) + (num%10))
sum_start = int((num//100000) + ((num//10000)%10) + ((num//1000)%10))
if sum_start == sum_end:
    print("Your number ticket WIIIN!!!")
else:
    print("Ooooh, no, sorry, lose...")
