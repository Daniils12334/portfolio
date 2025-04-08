#exception = An event that interrupts the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)
#            1.try, 2.except, 3.finally


# Python error documentation
# https://docs.python.org/3/library/exceptions.html


# 1 / 0 ZeroDivisionError
#1 + "1" TypeError
#int("pizza") ValueError invalid literal for int() with base 10" 'pizza'

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("Value cant be zero")
except ValueError:
    print("Enter numbers instead of strings")
# except Exception:                  # Microsoft style
    # print("something went wrong!") # Bad practise
finally:
    print("Do some cleanup here")

# 🧨 Что такое исключения в Python?

# Исключения — это ошибки, которые возникают во время выполнения программы. Python «выбрасывает» (raise) исключение, если происходит что-то неожиданное (например, деление на ноль, доступ к несуществующему файлу и т.д.).
# ✅ Пример: обработка исключения

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Нельзя делить на ноль!")

# 📌 Блок try — тут выполняется код, который может вызвать ошибку.
# 📌 Блок except — здесь обрабатываем ошибку, если она случилась.
# 🔁 Общая структура:

# try:
#     # потенциально опасный код
# except ТипИсключения:
#     # обработка исключения
# else:
#     # если ошибки не было
# finally:
#     # выполняется всегда (например, закрытие файла или соединения)

# 🎯 Примеры разных исключений:

# try:
#     lst = [1, 2, 3]
#     print(lst[5])
# except IndexError:
#     print("Элемент с таким индексом не существует!")

# try:
#     num = int("abc")
# except ValueError:
#     print("Невозможно преобразовать строку в число!")

# 💡 Обработка нескольких исключений:

# try:
#     x = int("abc")
# except (ValueError, TypeError):
#     print("Ошибка преобразования!")

# 🚨 Создание собственных исключений:

# class MyCustomError(Exception):
#     pass

# def do_something():
#     raise MyCustomError("Что-то пошло не так!")

# try:
#     do_something()
# except MyCustomError as e:
#     print(f"Поймали ошибку: {e}")

# 🔍 Почему это важно?

#     Исключения позволяют не ломать программу при ошибках.

#     Помогают логировать и анализировать проблемы.

#     Делают код читаемым и надёжным.