while True:
    try:
        n = int(input("Введіть число факторіала: "))
        if (1 <= n and n <= 2 * (10 ** 9)):
            zeros = 0
            while n > 0:
                n = n // 5
                zeros += n
            print(zeros)
            break
        else:
            print("Помилка - введено некоректне значення")
    except ValueError:
        print("Помилка - потрібно ввести лише цілі числа")