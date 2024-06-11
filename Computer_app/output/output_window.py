from tkinter import Tk, Label, Button
window = Tk()

window.geometry('1268x833+1+70')
window.resizable(False, False)
window.title('Дневник семян')
window.config(bg='green')

file_settings = open('settings.txt', 'r', encoding='utf-8')
f = file_settings.readlines()
file_settings.close()
if len(f) == 0:
    file_settings = open('settings.txt', 'r+', encoding='utf-8')
    lbl = Label(window, text="Давайте настроим приложение\nlet's set up the application\n让我们设置应用程序", bg='green', fg='white', font='Arial 35', justify='center')
    lbl.grid(row=0, column=0, columnspan=10)

    btn = Button(window, text='Дальше\nNext\n更远')
    btn.grid(row=1, column=10)
    file_settings.close()

window.mainloop()