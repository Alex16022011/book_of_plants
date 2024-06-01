from tkinter import Tk, Label, Button
window = Tk()

window.geometry('1268x833+1+70')
window.resizable(False, False)
window.title('Дневник семян')
window.config(bg='green')
if 
file_settings = open('C:/Users/МойКомпьютер/.vscode/book_of_plants/settings.txt', encoding='utf-8', )
f = file_settings.readlines()
file_settings.close()
if len(f) == 0:
    file_settings = open('C:/Users/МойКомпьютер/.vscode/book_of_plants/settings.txt', encoding='utf-8')
    lbl = Label(window, text="Давайте настроим приложение\nlet's set up the application\n让我们设置应用程序", bg='green', font='Arial 50')
    lbl.grid(row=0, column=0)

    btn = Button(window, text='Дальше\nNext\n更远')
    btn.grid(row=1, column=10)

window.mainloop()