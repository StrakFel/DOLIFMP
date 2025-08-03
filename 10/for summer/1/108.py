while True:
    try:
        numbers = list(map(int, input("Введіть 3 цілих числа не перевищують 1000 через пробіл: ").split()))
        if len(numbers) != 3:
            print("Помилка - потрібно ввести рівно три числа")
        elif len(set(numbers)) != 3:
            print("Помилка - числа повинні бути різними")
        elif any(abs(n) > 1000 for n in numbers):
            print("Помилка - числа за модулем не повинні перевищувати 1000")
        else:
            print(sorted(numbers)[1])
            break
    except ValueError:
        print("Помилка - потрібно ввести лише цілі числа")