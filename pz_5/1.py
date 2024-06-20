# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с 
#параметрами. Значения n и m программа должна запрашивать.
# #

def find_sum(n, m):
    # формула арефметической прогрессии 
    result = (m * (m + 1) - n * (n - 1)) / 2
    return result
n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))

result = find_sum(n, m)
print(f"Сумма чисел от {n} до {m}: {result}")
