def program_1():
    # Задача 1 "Арифметика"
    print(9 ** 0.5 * 5)

def program_2():
    # Задача 2 "Логика"
    print(9.99 > 9.98 and 1000 != 1000.1)

def program_3():
    # Задача 3 "Школьная загадка"
    print(2 * 2 + 2)
    print(2 * (2 + 2))
    print((2 * 2 + 2) == (2 * (2 + 2)))

def program_4():
    # Задача 4 "Первый после точки"
    print(int(float("123.456") * 10) % 10)



if __name__ == '__main__':
    program_1()
    program_2()
    program_3()
    program_4()