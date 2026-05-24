
from tkinter import * # Импортируем все из библиотеки tkinter для создания графического интерфейса
from tkinter import ttk # Импортируем ttk для использования стилей в виджетах

# Генератор паролей используя tkinter от lazyyy-dev
# Версия 1.0
# Дата создания: 24-05-2026

# Создание символов для генерации пароля
characters = 'fkgmefoigjeroigprjgoiergmriogRTIJGHERMFRKFKVVMMGG123345678990'

# Backend логика для генерации пароля

def generate():
    import random
    import time
    label_animation.config(text="Генерируем пароль...")  # Показываем анимацию
    result_password.config(text="")  # Убираем вывод полученного пароля, пока не будет готов результат
    root.update()  # Обновляем интерфейс, чтобы анимация отобразилась
    time.sleep(2)  # Имитируем задержку
    label_animation.config(text="")  # Скрываем анимацию после генерации
    # Генерируем пароль и отображаем результат
    try:
        length = int(type_symbols.get()) # Получаем количество символов из поля ввода и преобразуем его в целое число
        if length <= 0: # Проверяем, что введенное число положительное
            result_password.config(text="Пожалуйста, введите положительное число.", fg='red')
            return
        if length > 50: # Проверяем, что введенное число не превышает количество доступных символов
            result_password.config(text="Вы превысили лимит символов. Попробуйте снова.", fg='red')
            return 
        password = ''.join(random.choice(characters) for _ in range(length)) # Генерируем пароль, выбирая случайные символы из строки characters
        result_password.config(text=f"Ваш пароль: {password}", fg='green') # Отображаем сгенерированный пароль в лейбле result_password
    except ValueError: # Обрабатываем исключение, если введенное значение не является числом
        result_password.config(text="Пожалуйста, введите корректное число.", fg='red') 

# Frontend логика для создания графического интерфейса приложения

# 1. Создание окна приложения
root = Tk()
root.title("Password Generator - by lazyyy-dev")
root.geometry("600x200")
root.resizable(False, False)

# 2. Создание фрейма для header панели
frame_header = Frame(relief=SOLID, bg='#7FFFD4')
header_text = Label(frame_header, text="Генератор паролей", background='#7FFFD4', font=("Verdana", 15, 'bold'))
header_text.pack(anchor=N)
frame_header.pack(anchor=N, fill=BOTH)

# 3. Создание лейбла для ввидения пользователя в принцип работы приложения
type_symbols_info = Label(root, text="Введите количество символов для создания пароля:", font=("Arial", 11, 'bold'))
type_symbols_info.place(x = 10, y = 50)

# 3. Создания стиля для поля ввода кол-ва символов
style = ttk.Style().theme_use('clam')

# 4. Создание поля для ввода количества символов
type_symbols = ttk.Entry(root, style='Clam.TEntry')
type_symbols.place(x = 440, y = 52)

# 5. Создание кнопки для генерации пароля
generate_password = Button(root, text='Сгенерировать пароль', font=("Verdana", 11), bg='#7FFFD4', relief=SOLID, command=generate)
generate_password.place(x = 200, y = 100)

# 6. Создание лейбла с анимацией перед получением результата
label_animation = Label(root, text="Генерируем пароль...", font=("Arial", 10, 'italic'), fg='blue')
label_animation.place(x = 220, y = 150)
label_animation.config(text="")  # Скрываем анимацию по умолчанию

# 7. Создание лейбла для отображения сгенерированного пароля
result_password = Label(root, text="Ваш пароль: ", font=("Arial", 12, 'bold'), fg='green')
result_password.config(text="")  # Убираем вывод полученного пароля, пока не будет готов результат
result_password.place(x = 10, y = 180)

root.mainloop() # Запуск главного цикла приложения, который позволяет окну оставаться открытым и реагировать на события