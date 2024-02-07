import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import main
import time
import unittest_sort


"""Методы кнопок"""

size = 10
random_numbers = []
def generate_random_numbers():
    """Генерация рандомных чисел"""
    random_numbers = [random.randint(-10000, 100000) for x in range(size)]
    return random_numbers


def insert_random_numbers():
    """Вставка в таблицу значений"""
    global random_numbers
    random_numbers = generate_random_numbers()
    for row in table2.get_children():
        table2.delete(row)
    for i, number in enumerate(random_numbers):
        table2.insert('', 'end', values=(number,))


def button_go_clicked(random_numbers):
    global sorted_numbers
    # Проверяем, есть ли случайные числа
    if entry.get():
        values = entry.get().split(',')
        try:
            random_numbers = [float(value.strip()) for value in values]  # Преобразуем введенные значения в числа
        except ValueError:
            messagebox.showerror("Ошибка", "Невозможно преобразовать введенные значения в числа")
            return
    elif random_numbers:
        # Если поле ввода пустое, но есть сгенерированные случайные числа, берем их для сортировки
        pass  # Ничего делать не нужно, так как random_numbers уже содержит нужные значения
    else:
        # Если ничего нет ни в поле ввода, ни в рандомных числах, выводим сообщение об ошибке
        messagebox.showerror("Ошибка", "Введите значения или воспользуйтесь кнопкой для генерации случайных чисел")
        return

    selected_sort_method = combo_box.get()
    func_map = {'Сортировка пузырьком': main.bubble_sort,
                'Сортировка вставками': main.insertion_sort,
                'Сортировка выбором': main.selection_sort}



    if selected_sort_method in func_map:
        sort_func = func_map[selected_sort_method]
        sorted_numbers = sort_func(random_numbers)  # Сохраняем отсортированные данные
        start_time = time.time()
        end_time = time.time() - start_time
        # messagebox.showerror('Время', 'Время: %s секунд' % end_time)
        print(sorted_numbers)
        insert_sorted_numbers_to_table()  # Вставляем отсортированные данные в таблицу


        """Вывод времени сортировки"""
        result_window = tk.Toplevel(root)
        result_window.title("Результат сортировки")
        result_window.geometry("300x100")

        result_label = tk.Label(result_window, text="Время сортировки: {:.6f} секунд".format(end_time))
        result_label.pack()


    else:
        messagebox.showerror('Ошибочка','Выбран некорректный метод сортировки')

def insert_sorted_numbers_to_table():
    """Вставка отсортированных чисел в таблицу"""
    for row in table1.get_children():
        table1.delete(row)
    for i, number in enumerate(sorted_numbers):
        table1.insert('', 'end', values=(number,))

def add_manual_number():
    global random_numbers
    values = entry.get().split(',')
    for value in values:
        try:
            number = float(value.strip())  # Преобразуем введенное значение в число
            random_numbers.append(number)  # Добавляем число в список
            print("Введенное число добавлено в random_numbers:", number)
        except ValueError:
            print("Ошибка: Невозможно преобразовать введенное значение в число")
    entry.delete(0, tk.END)  # Очищаем поле ввода




"""Графический интерфейс"""

def button_click():
    text = entry.get()
    selected_option = combo_box.get()
    label.config(text=f'Text: {text}, Option: {selected_option}')


def show_tooltip(event):
    tooltip.place(x=label_sequence.winfo_width() + 5, y=0)

def hide_tooltip(event):
    tooltip.place_forget()

# Создаем главное окно
root = tk.Tk()
root.title("Прекрасное далеко")
root.geometry("500x500")

# Создаем виджеты
frame_left = tk.Frame(root)
frame_left.pack(anchor="n", padx=10, pady=10)

frame_nsew = tk.Frame(root)
frame_nsew.pack(expand=True, fill="both")


label_sequence = tk.Label(frame_left, text="Последовательность чисел:")
label_sequence.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(frame_left, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

label_sequence = tk.Label(frame_left, text="Или вы можете:")
label_sequence.grid(row=1, column=0, padx=10, pady=10)

button_insert = tk.Button(frame_left,text="Вставить случайные числа", command = insert_random_numbers)
button_insert.grid(row=1, column=1, padx=10, pady=10)

label_sort = tk.Label(frame_left, text="Выберите вид сортировки:")
label_sort.grid(row=2, column=0, padx=10, pady=10)

combo_box = ttk.Combobox(frame_left, values=["Сортировка пузырьком", 'Сортировка вставками', 'Сортировка выбором'])
combo_box.current(0)
combo_box.grid(row=2, column=1, padx=10, pady=10)


table1 = ttk.Treeview(frame_nsew, columns=("Numbers"), show="headings", height=10)
table1.heading("Numbers", text="Итог сортировки")
table1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


table2 = ttk.Treeview(frame_nsew, columns=("Numbers"), show="headings", height=10)
table2.heading("Numbers", text="Случайные числа")
table2.grid(row=0, column=1, padx=50, pady=10, sticky="nsew")


button_go = tk.Button(frame_left, text="Start", command=lambda: button_go_clicked(random_numbers), background="light green", height=2, width=20)
button_go.grid(row=3, columnspan=2, padx=10, pady=10)


# Запускаем основной цикл обработки событий
root.mainloop()


