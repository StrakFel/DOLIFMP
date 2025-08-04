import random
import math

# Допоміжні функції
def create_random_numbers(): # Функція для задання випадкової кількості змінних
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    n = random.randint(1, 10)
    x = random.randint(1, 100)
    y = random.randint(1, 10)
    return num_1, num_2, n, x, y

def check_numbers(num_1, num_2, x, y): # Функція для перевірки пар чисел
    num_1, num_2 = max(num_1, num_2), min(num_1, num_2)
    x, y = max(x, y), min(x, y)
    return num_1, num_2, x, y

def generate_with_limit(): # Функція для з'єднання функцій create_random_numbers та check_numbers
    num_1, num_2, n, x, y = create_random_numbers()
    num_1, num_2, x, y = check_numbers(num_1, num_2, x, y)
    return num_1, num_2, n, x, y

def value_equation(user_choice): # Функція для перевірки введення користувача
    if user_choice == '1':
        return create_equation_plus()
    elif user_choice == '2':
        return create_equation_minus()
    elif user_choice == '3':
        return create_equation_multiplication()
    elif user_choice == '4':
        return create_equation_division()
    elif user_choice == '5':
        return create_equation_power()
    elif user_choice == '6':
        return create_equation_square_root()
    elif user_choice == '7':
        return create_equation_factorial()
    elif user_choice == '8':
        return create_equation_subfactorial()
    elif user_choice == '9':
        return all_in()

# Функції для майстрів
def factorial(n): # Функція факторіалу
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def create_equation_factorial(): # Функція створення рівняння факторіалу
    _, _, n, _, _ = generate_with_limit()
    equation_print = f'{n}!'
    equation_result = factorial(n)
    return equation_print, equation_result

def subfactorial(n): # Функція субфакторіалу
    equation_result = 0
    for k in range(n + 1):
        equation_result += (-1) ** k / math.factorial(k)
    return round(math.factorial(n) * equation_result)

def create_equation_subfactorial():  # Функція створення рівняння субфакторіалу
    _, _, n, _, _ = generate_with_limit()
    equation_print = f'!{n}'
    equation_result = subfactorial(n)
    return equation_print, equation_result

def power(x, y): # Функція відтворення у ступінь
    equation_result = 1
    for i in range(y):
        equation_result *= x
    return equation_result

def create_equation_power(): # Функція створення рівняння відтворення у ступінь
    _, _, _, x, y = generate_with_limit()
    equation_print = f'{x}^{y}'
    equation_result = power(x, y)
    return equation_print, equation_result

def square_root(): # Функція для відтворення числа в корінь
    num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256,
                    289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841,
                    900, 961]
    return random.choice(num)

def create_equation_square_root(): # Функція для відтворення числа в корінь
    num = square_root()
    equation_print = f'√{num}'
    equation_result = math.isqrt(num)
    return equation_print, equation_result

# Функции для создания уравнения
def create_equation_plus(): # Функція для тренування із плюсом
    num_1, num_2, _, _, _ = generate_with_limit()
    equation_print = f'{num_1} + {num_2}'
    equation_result = num_1 + num_2
    return equation_print, equation_result

def create_equation_minus(): # Функція для тренування з мінусом
    num_1, num_2, _, _, _ = generate_with_limit()
    equation_print = f'{num_1} - {num_2}'
    equation_result = num_1 - num_2
    return equation_print, equation_result

def create_equation_multiplication(): # Функція для тренування з множенням
    num_1, num_2, _, _, _ = generate_with_limit()
    equation_print = f'{num_1} * {num_2}'
    equation_result = num_1 * num_2
    return equation_print, equation_result

def create_equation_division(): # Функція для тренування з відніманням
    while True:
        num_1, num_2, _, _, _ = generate_with_limit()
        if num_1 % num_2 == 0:
            equation_print = f'{num_1} / {num_2}'
            equation_result = int(num_1 / num_2)
            return equation_print, equation_result

def all_in(): # Функція з усіма рівняннями цієї програми
    choices = ['1', '2', '3', '4', '5', '6', '7', '8']
    user_choice = random.choice(choices)
    equation_print, equation_result = value_equation(user_choice)
    return equation_print, equation_result

# Функція для перевірки правильності відповіді користувача
def check_answer(user_answer, correct_result):
    return user_answer == correct_result