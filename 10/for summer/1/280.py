import math

while True:
    try:
        n = input("Введіть два числа: об'єми двох куч піску (від 1 до 2^16) через пробіл: ")
        parts = n.strip().split()
        if len(parts) != 2:
            print("Помилка: введіть рівно два числа")
            continue
        n, m = map(int, parts)
        if 1 <= n <= 2**16 and 1 <= m <= 2**16:
            res = math.gcd(n, m)
            print(f"Максимальна місткість відра: {res}")
            break
        else:
            print("Введено некоректне значення, спробуйте ще раз")
    except ValueError:
        print("Помилка - потрібно ввести лише ціле число")