import tkinter as tk
from translate import Translator


# Функція для перекладу
def translate():
    text = entry.get()
    language_from = language_from_var.get()
    language_to = language_to_var.get()

    translator = Translator(from_lang=language_from, to_lang=language_to)
    translated = translator.translate(text)
    result_label.config(text=translated)


# Створення основного вікна
root = tk.Tk()
root.title("Перекладач")
root.geometry("500x150")

# Створення елементів інтерфейсу
entry = tk.Entry(root, width=40)
entry.pack(side="top")
entry.insert(0, "привіт")

# Варіанти для вибору мов
languages = ['uk', 'en', 'es', 'fr', 'de', 'it']
language_from_var = tk.StringVar(value='uk')
language_to_var = tk.StringVar(value='en')

# Створення меню для вибору мов
language_from_menu = tk.OptionMenu(root, language_from_var, *languages)
language_from_menu.pack(side="left")

language_to_menu = tk.OptionMenu(root, language_to_var, *languages)
language_to_menu.pack(side="right")

# Кнопка перекладу
translate_button = tk.Button(root, text="𓂃🖊", command=translate)
translate_button.pack(anchor="center")

# Мітка для відображення перекладеного тексту
result_label = tk.Label(root,
                        text="тут буде переклад",
                        font=("Arial", 12),
                        fg='purple')
result_label.pack(side="bottom")

root.mainloop()
