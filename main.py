from datetime import datetime
from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('Секундомер')
root.resizable(width=False, height=False)

temp = 0
after_id = ''


# Рекурсивная функция для обновления функции каждую секунду
def sec():
    global temp, after_id
    after_id = root.after(1000, sec)
    # устанавливаем формат времени
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    # Выводим наш результат
    l1['text'] = str(f_temp)
    temp += 1


def start():
    # Кнопка буде становится не активной после нажатия на старт
    btn_start['state'] = 'disabled'
    btn_stop.place()
    btn_stop['state'] = 'normal'
    sec()


def stop():
    btn_stop['state'] = 'disabled'
    btn_continue['state'] = 'normal'
    btn_reset['state'] = 'normal'
    root.after_cancel(after_id)


def set_continue():
    btn_continue['state'] = 'disabled'
    btn_stop['state'] = 'normal'
    btn_reset['state'] = 'normal'
    sec()


def reset():
    global temp
    btn_reset['state'] = 'disabled'
    btn_stop['state'] = 'disabled'
    btn_continue['state'] = 'disabled'
    btn_start['state'] = 'normal'
    temp = 0
    l1['text'] = '00:00'


l1 = Label(root, text='00:00', width=25, height=10, font=("Conic Sans MS", 25, 'bold'))
l1.place(relx=0.5, rely=0.1, anchor=CENTER)

btn_start = Button(root, text='Старт', font=('Arial 35', 16), fg='red', bg='black', command=start)
btn_start['state'] = 'normal'
btn_start.place(relx=0.5, rely=0.25, anchor=CENTER)

btn_stop = Button(root, text='Стоп', font=('Arial 35', 16), fg='yellow', bg='black', command=stop)
btn_stop['state'] = 'disabled'
btn_stop.place(relx=0.5, rely=0.4, anchor=CENTER)

btn_continue = Button(root, text='Продолжить', font=('Arial 35', 16), fg='light Green', bg='black', command=set_continue)
btn_continue['state'] = 'disabled'
btn_continue.place(relx=0.5, rely=0.55, anchor=CENTER)

btn_reset = Button(root, text='Перезагрузить', font=('Arial 35', 16), fg='orange', bg='black', command=reset)
btn_reset['state'] = 'disabled'
btn_reset.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()