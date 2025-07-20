import tkinter as tk  # import *
# from tkinter import *

win = tk.Tk()
photo = tk.PhotoImage(file='icon_mic.png')
win.iconphoto(False, photo)
win.config(bg='red')
win.title("звуковой помощник")  # название окна
win.geometry('1000x600+180+140')  # +180+140 - смещение места поведения окна
win.minsize(800, 500)
win.maxsize(1200, 700)
win.resizable(True, True)  # фиксация размеров окна
greeting = tk.Label(text="Привет, Tkinter!")
greeting.pack()
win.mainloop()
