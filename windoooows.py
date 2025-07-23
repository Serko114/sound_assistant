import tkinter as tk  # import *
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
# from tkinter import *

# ------------------ блок вытаскивающий введенную фразу --------------------


def show_message():
    label["text"] = entry.get()     # получаем введенный текст
    print(str(label["text"]).lower())


def show_message():
    label["text"] = entry.get()     # получаем введенный текст
    print(str(label["text"]).lower())

# --------------------------------------------------------------------------


win = tk.Tk()
# вставляет картинку в верхнем левом углу
photo = tk.PhotoImage(file='icon_mic.png')
win.iconphoto(False, photo)
# win.config(bg='yellow')
win.title("голосовой помощник")  # название окна
win.geometry('650x450+1580+240')  # +480+140 - смещение места поведения окна
# win.minsize(800, 500)
# win.maxsize(1200, 700)
# win.resizable(True, True)  # фиксация размеров окна
# ----------------------------------поле_ввода ключевого слова----------------------------------------
text_1 = '''   1.      Для использования звукового помощника необходимо ввести ключевое слово, при произношении   
            которого помощник будет просыпаться (помощник - женщина, язык ввода - русский, регистр - неважен)'''
info_1 = ttk.Label(win, text=text_1)
info_1.grid(column=0, row=0, columnspan=25)  # grid(column=0, row=1)


propusk_0 = ttk.Label(win, text=' ')
propusk_0.grid(column=0, row=1, columnspan=8)
# ключевое слово -> комментарий
info_lab = ttk.Label(win, text='   Введите ключевое слово:  ')
entry = ttk.Entry()  # ключевое слово -> поле ввода
# ключевое слово -> кнопка
enter_button = ttk.Button(win, text='Фиксация', command=show_message)
# ключевое слово -> показ ключевого слова
# -> еще не введено')
label = tk.Label(text='...................', fg='green')
# -> еще не введено')
info_lab.grid(column=0, row=2)  # ключевое слово -> активация комментария
entry.grid(column=2, row=2)  # ключевое слово -> активация поля ввода
enter_button.grid(column=3, row=2)  # ключевое слово -> активация кнопки
label.grid(column=6, row=2)  # ключевое слово -> показ ключевого слова

# entry.grid()
# -------------------------------------------------------------------------------------------------------------
# --------------------------кнопка_включено---------------------------------
propusk_1 = ttk.Label(win, text=' ')
propusk_1.grid(column=0, row=3, columnspan=8)
propusk_2 = ttk.Label(win, text=' ')
propusk_2.grid(column=0, row=5, columnspan=8)
text_2 = '''   2.      Выберите необходимость озвучки:'''
info_2 = ttk.Label(win, text=text_2)
info_2.grid(column=0, row=6, columnspan=25,
            sticky=tk.W)  # grid(column=0, row=1)
# -------------------------------------------------------------------------------------------------------------

position = {"padx": 6, "pady": 6, }

sound = "Со звуком"
no_sound = "Без звука"
javascript = "JavaScript"
# по умолчанию будет выбран элемент с value=java
lang = tk.StringVar(value=sound)
header = tk.Label(textvariable=lang, fg='green')
header.grid(column=2, row=7)  # , sticky=tk.W)

python_btn = ttk.Radiobutton(text=sound, value=sound, variable=lang)
python_btn.grid(column=0, row=7)  # , sticky=tk.W)

javascript_btn = ttk.Radiobutton(
    text=no_sound, value=no_sound, variable=lang)
javascript_btn.grid(column=1, row=7)  # , sticky=tk.W)

# java_btn = ttk.Radiobutton(text=javascript, value=javascript, variable=lang)
# java_btn.grid(column=2, row=7, sticky=tk.W)
# btn.grid(column=2, row=8)

# НЕПРАВИЛЬНО ЖМЕШЬ, ЕЩЕ РАЗ ПОПРОБУЙ; ВО, ДРУГОЕ ДЕЛО, ГОВОРИ !
# СЛАБО НАЖАЛ, ЕЩЕ РАЗ
# ЧО ПЛОХО ЖМЕМ, ЕЩЕ РАЗ
# --------------------------кнопка_включено---------------------------------
# def checkbutton_changed():
#     if enab.get() == 1:
#         showinfo(title="Info", message="Запись")
#     else:
#         showinfo(title="Info", message="Отключено")


# enab = tk.IntVar()


# enabled_checkbutton = ttk.Checkbutton(
#     text="Включить", variable=enab, command=checkbutton_changed)
# enabled_checkbutton.grid(padx=6, pady=6)  # , anchor=NW)
# --------------------------------------------------------------------------

win.mainloop()
# name = entry.get()
# lst.append(name)
# print(label["text"])
