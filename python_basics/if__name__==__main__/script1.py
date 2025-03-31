#if __name__ == __main__: (this script can be imported OR run standalone)
#                          Functions and classes in this module can be refused
#                          without the main block of code executing

def fav_food(food):
    print(f"{food} is your favourite food")

def main():
    # Your program goes here
    print('danbar script1')
    fav_food("makaroni")

if __name__ == '__main__':
    main()

def test():
    print("Этот код можно вызвать из другого модуля")

if __name__ == "__main__":
    print("Этот код выполняется только при запуске файла")
