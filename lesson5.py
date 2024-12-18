import tkinter as tk
from tkinter import messagebox


def show_text():
    if not entry.get():
        messagebox.showerror('Error', 'Empty field')
    else:
        print("Entered text:", entry.get())


app = tk.Tk()
app.title('First App')
app.geometry("400x150")


entry = tk.Entry(app)
entry.pack()


button = tk.Button(app, text='Show', command=show_text)
button.pack()

app.mainloop()