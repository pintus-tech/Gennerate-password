import tkinter as tk
from tkinter import messagebox
import random


def genera_password():
    minuscolo = "abcdefghijklmnopqrstuvwxyz"
    maiuscolo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    simboli = "#@{}[]*_-.:,;!\/()=?$%&+|°><"
    numeri = "0123456789"

    all = minuscolo + maiuscolo + simboli + numeri
    lunghezza = 25
    password = "".join(random.sample(all, lunghezza))
    password_label.config(text=password)
    copia_button.pack()


def copia_password():
    password = password_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copiato", "La password è stata copiata negli appunti")


root = tk.Tk()
root.title("Generatore di Password")


genera_button = tk.Button(root, text="Genera Password", command=genera_password)
genera_button.pack(pady=10)


password_label = tk.Label(root, text="", font=("Helvetica", 12))
password_label.pack(pady=10)


copia_button = tk.Button(root, text="Copia Password", command=copia_password)
copia_button.pack(pady=10)
copia_button.pack_forget()


root.mainloop()ennerate-password

