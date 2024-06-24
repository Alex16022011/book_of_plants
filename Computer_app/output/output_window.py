from tkinter import Tk, Label, Button, Entry
from Computer_app.analysing.is_right_registration import is_right_registration
import os
window = Tk()

window.geometry('1268x833+1+70')
window.resizable(False, False)
window.title('Дневник семян')
window.config(bg='green')

file_settings = open('settings.txt', 'r', encoding='utf-8')
f = file_settings.readlines()
file_settings.close()
counter = 1
lbl3 = Label(window, text='Заполните все поля', font='Arial 20', bg='red', fg='white')
# 0 = NO
# 1 = YES
which_number_for_constants_for_login_will_be = 0
which_number_for_constants_for_password_will_be = 0


def list_page():
    global counter
    global entr1
    global entr2
    global lbl3
    global which_number_for_constants_for_login_will_be
    global which_number_for_constants_for_password_will_be
    if counter == 1:
        if which_number_for_constants_for_login_will_be == 0:
            # 0 -> NO
            # 1 -> YES and if it was placed -> destroy
            need_place_error_or_not = 0
        else:
            # 0 -> NO
            # 1 -> YES and if it was placed -> destroy
            need_place_error_or_not = 1
        login = entr0.get()
        if len(login) == 0 and need_place_error_or_not == 0:
            need_place_error_or_not = 1
            lbl3.place(x=500, y=500)
            print('FIRST IF IS DID')
            which_number_for_constants_for_login_will_be = 1
        if need_place_error_or_not == 1 and len(login) != 0:
            lbl3.destroy()
            lbl3 = Label(window, text='Заполните все поля', font='Arial 20', bg='red', fg='white')
            need_place_error_or_not = 0
            which_number_for_constants_for_login_will_be = 0
            print('SECOND IF IS DID')
        if need_place_error_or_not == 0:
            list1 = {'login': login}
            # lbl3.destroy()
            lbl0.destroy()
            entr0.destroy()
            lbl1 = Label(window, text='Введите ваш пароль:', font='Arial 20', bg='green', fg='white')
            entr1 = Entry(window, font='Arial 20', bg='white', fg='black')
            lbl1.place(x=500, y=200)
            entr1.place(x=490, y=250)

            lbl2 = Label(window, text='Повторите ваш пароль:', font='Arial 20', bg='green', fg='white')
            entr2 = Entry(window, font='Arial 20', bg='white', fg='black')
            lbl2.place(x=500, y=400)
            entr2.place(x=490, y=450)
            counter += 1
            print(list1)
            del which_number_for_constants_for_login_will_be
    if counter == 2:
        # password1 = entr1.get()
        # password2 = entr2.get()
        # if which_number_for_constants_for_password_will_be == 1:
        #     if password1 != password2:
        #         lbl3 = Label(window, text='Пароли не совпадают', font='Arial 20', bg='red', fg='white')
        #         lbl3.place(x=500, y=600)
        #     elif (len(password1) == 0 or len(password2) == 0) and (password1 != '' and password2 != ''):
        #         lbl3 = Label(window, text='Заполните все поля', font='Arial 20', bg='red', fg='white')
        #         lbl3.place(x=500, y=600)
        # else:
        #     pass
        # else:
        #     list1['password'] = password1
        #     print(list1)
        counter += 1
    if counter == 3:
        counter += 1
    if counter == 4:
        counter += 1


def start_presentation():
    def open_powerpoint_presentation(file_path):
        os.system(f"start powerpnt {file_path}")

    file_path = "C:/Users/user/PycharmProjects/book_of_plants2/Презентация_проекта_book_of_plants_(Дневник_семян).pptx"
    open_powerpoint_presentation(file_path)


if len(f) == 0:
    file_settings = open('settings.txt', 'r+', encoding='utf-8')

    lbl0 = Label(window, text='Введите ваш логин:', font='Arial 20', bg='green', fg='white')
    lbl0.place(x=500, y=250)
    entr0 = Entry(window, font='Arial 20', bg='white', fg='black')
    entr0.place(x=480, y=300)
    # btn0 = Button(window, text='Отправить', font='Arial 20', command=is_right_registration)
    # btn0.grid(row=2, column=0, padx=480, pady=(300, 0))
    btn0 = Button(window, text='Далее', font='Arial 30', command=list_page)
    btn0.place(x=1100, y=730)

    # lbl1 = Label(window, text='Введите ваш пароль:', font='Arial 20', bg='green', fg='white')
    # lbl1.grid(row=0, column=1)
    # entr1 = Entry(window, font='Arial 20', bg='white', fg='black')
    # entr1.grid(row=1, column=1, padx=7)
    #
    # lbl2 = Label(window, text='Введите ваш логин:', font='Arial 20', bg='green', fg='white')
    # lbl2.grid(row=0, column=2)
    # entr2 = Entry(window, font='Arial 20', bg='white', fg='black')
    # entr2.grid(row=1, column=2, padx=7)
    #
    # lbl3 = Label(window, text='Введите ваш логин:', font='Arial 20', bg='green', fg='white')
    # lbl3.grid(row=0, column=3)
    # entr3 = Entry(window, font='Arial 20', bg='white', fg='black')
    # entr3.grid(row=1, column=3, padx=7)
    file_settings.close()


def to_bind(event):
    list_page()


window.bind('<Return>', to_bind)

window.mainloop()