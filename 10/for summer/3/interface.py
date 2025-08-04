import time
import tkinter as tk
from tkinter import messagebox
from logic import value_equation  # Імпорт функції генерації рівнянь

class MathTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Математичний тренажер")
        self.score = 0  # Рахунок користувача
        self.lives = 3  # Кількість життів
        self.rounds = 0  # Кількість раундів (спроб)
        self.start_time = time.time()  # Час початку гри
        self.last_result = None  # Останній результат для уникнення повторів
        self.create_menu()  # Створення меню вибору режиму

    def create_menu(self):
        self.clear_window()  # Очищення вікна
        tk.Label(self.root, text="Виберіть режим:", font=("Arial", 14)).pack(pady=10)

        modes = [
            ("Плюс", '1'), ("Мінус", '2'), ("Множення", '3'), ("Ділення", '4'),
            ("Ступінь", '5'), ("Корінь", '6'), ("Факторіал", '7'),
            ("Субфакторіал", '8'), ("All-In", '9')
        ]

        # Створення кнопок для кожного режиму
        for name, mode in modes:
            tk.Button(self.root, text=name, width=25, command=lambda m=mode: self.start_game(m)).pack(pady=2)

        # Кнопка виходу з програми
        tk.Button(self.root, text="Вихід", width=25, command=self.quit_program).pack(pady=10)

    def start_game(self, mode):
        self.mode = mode  # Встановлення вибраного режиму
        self.score = 0  # Скидання рахунку
        self.lives = 3  # Відновлення життів
        self.rounds = 0  # Скидання кількості раундів
        self.last_result = None  # Скидання останнього результату
        self.start_time = time.time()  # Фіксація часу початку гри
        self.next_equation()  # Показати перше рівняння

    def next_equation(self):
        self.eq_text, self.eq_result = value_equation(self.mode)  # Отримання нового рівняння і відповіді
        # Якщо результат повторюється, генеруємо просте додавання для унікальності
        if self.eq_result == self.last_result:
            self.eq_text, self.eq_result = value_equation('1')  # подстраховка (режим "плюс")
        self.last_result = self.eq_result  # Запам'ятовуємо результат
        self.show_game_ui()  # Показати інтерфейс з новим рівнянням

    def show_game_ui(self):
        self.clear_window()  # Очищення вікна
        # Відображення рахунку і кількості життів
        tk.Label(self.root, text=f"Рахунок: {self.score}   Життя: {self.lives}", font=("Arial", 12)).pack()
        # Відображення рівняння
        tk.Label(self.root, text=self.eq_text + " =", font=("Arial", 24)).pack(pady=20)

        self.answer_var = tk.StringVar()  # Змінна для введення відповіді користувача
        tk.Entry(self.root, textvariable=self.answer_var, font=("Arial", 18)).pack()  # Поле введення відповіді
        tk.Button(self.root, text="Перевірити", command=self.check_answer).pack(pady=10)  # Кнопка перевірки відповіді
        tk.Button(self.root, text="Меню", command=self.back_to_menu).pack()  # Кнопка повернення в меню

    def check_answer(self):
        try:
            user_input = int(self.answer_var.get())  # Спроба перетворити введене в ціле число
        except ValueError:
            messagebox.showerror("Помилка", "Введіть ціле число")  # Повідомлення про помилку
            return

        # Перевірка відповіді
        if user_input == self.eq_result:
            self.score += 1  # Збільшуємо рахунок, якщо правильно
            messagebox.showinfo("Вірно", "Молодець!")  # Повідомлення про правильну відповідь
        else:
            self.lives -= 1  # Віднімаємо життя при помилці
            messagebox.showwarning("Невірно", f"Помилка! {self.eq_text} = {self.eq_result}")  # Повідомлення про помилку

        self.rounds += 1  # Збільшуємо кількість раундів

        # Перевірка, чи закінчилась гра (життя = 0)
        if self.lives <= 0:
            self.game_over()
        else:
            self.next_equation()  # Наступне рівняння

    def back_to_menu(self):
        self.create_menu()  # Повернення в меню

    def clear_window(self):
        # Видаляємо всі віджети у вікні (для оновлення UI)
        for widget in self.root.winfo_children():
            widget.destroy()

    def quit_program(self):
        # Обчислення часу гри
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)
        messagebox.showinfo("Вихід", f"До зустрічи!")
        self.root.destroy()  # Закриваємо вікно

    def game_over(self):
        # Показуємо повідомлення про кінець гри з підсумками
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)
        avg_time = round(total_time / self.rounds, 2) if self.rounds > 0 else 0
        messagebox.showinfo(
            "Гра закінчена",
            f"Гру завершено!\n"
            f"Рахунок: {self.score}\n"
            f"Час гри: {total_time} секунд\n"
            f"Середній час на відповідь: {avg_time} секунд"
        )
        self.create_menu()  # Повертаємося в меню після завершення