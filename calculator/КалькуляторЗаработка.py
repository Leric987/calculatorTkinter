from tkinter import *

def calculation():
    earnings = float(hourly.get()) * float(hours.get())
    result['text'] = f"{name.get()} заработал {earnings}Р на этой неделею"
    result.pack()


root = Tk()
root.title('Калькулятор заработка')
root.geometry('500x310')
root.resizable(width=False, height=False)
root['bg'] = 'black'

Label(root, text = 'Введите имя сотрудника:', font='arial 15 bold', fg='pink', bg='black').pack(pady=5)

name = Entry(root, font='Arial 13 bold')
name.pack(pady=5)

Label(root, text='Почасовая оплата сотрудника:', font='arial 15 bold', fg='pink', bg='black').pack(pady=5)

hourly = Entry(root, font='Arial 13 bold')
hourly.pack(pady=5)

Label(root, text='Кол-во часов проработанных за неделю:', font='arial 15 bold', fg='pink', bg='black').pack(pady=5)

hours = Entry(root, font='Arial 13 bold')
hours.pack(pady=5)

btn = Button(root, text='Рассчитать',  font='Arial 15 bold', command=calculation)
btn.pack(pady=5)

result = Label(root, font='arial 15 bold', fg='pink', bg='black')

root.mainloop()