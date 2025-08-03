while True:
    try:
        n, m = map(int, input("Введіть розміри шахівниці n×m (від 1 до 20): ").split())
        if 1 <= n <= 20 and 1 <= m <= 20:
            result = (n - 1) + (m - 1)
            print(f"Кількість клітин, на які тура може переміститися за один хід: {result}")
            break
        else:
            print("Введено некоректне значення, спробуйте ще раз")
    except ValueError:
        print("Помилка - потрібно ввести лише цілі числа")