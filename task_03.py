# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input('Введите, номер месяца: ')
month = int(user_input)
month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]
month28 = [2]
if month in month31:print(31)
elif month in month30:print(30)
elif month in month28:print(28)
else: print('Нет такого месяца.')
  
# Хорошо. Если интересно то моэжно сделать еще так
# Решение 2
import calendar as cl  # используем модуль для получения функции

year_input = input("Введите год: ")
month_input = input("Введите номер месяца: ")

year = int(year_input)
month_ = int(month_input)
print(cl.monthrange(year, month_))
