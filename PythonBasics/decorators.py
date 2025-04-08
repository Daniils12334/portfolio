#Decorator = A function that extends the behaviour of another function
#            w/o modifying the base functions
#            Pass the base function as an argument to the decorator

#            @add_spronkles
#            get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print("You add sprinkles")        
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("You add fudge")
        func(*args,**kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print("Here is your {flavor} icecream: ")

get_ice_cream("vanilla")

# 📌 Основная идея

# Декоратор — это функция, которая принимает другую функцию и возвращает новую функцию с дополнительным поведением.
# ✅ Простой пример

# def my_decorator(func):
#     def wrapper():
#         print("Что-то происходит до вызова функции.")
#         func()
#         print("Что-то происходит после вызова функции.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Привет!")

# say_hello()

# 🔍 Вывод:

# Что-то происходит до вызова функции.
# Привет!
# Что-то происходит после вызова функции.

# ⚙️ То же без синтаксиса @

# decorated = my_decorator(say_hello)
# decorated()

# 📦 Декоратор с аргументами функции

# def log_args(func):
#     def wrapper(*args, **kwargs):
#         print(f"Аргументы: {args}, {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @log_args
# def add(a, b):
#     return a + b

# print(add(3, 4))

# 💡 Декоратор с аргументами (фабрика декораторов)

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def greet():
#     print("Привет!")

# greet()

# 📚 Примеры использования в реальных задачах:

#     Логирование

#     Кэширование (@lru_cache)

#     Проверка прав

#     Тайминг выполнения

#     Ретраи запросов к API и т.п.