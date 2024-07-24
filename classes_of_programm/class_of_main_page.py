import sys

sys.path.append('.')
from customtkinter import *
from Computer_app.about_computer.size_of_screen import know_the_size_of_screen


class MainPage():
    def title_main(self, window, width1: int, height1: int):
        frm = CTkFrame(master=window, width=width1, height=height1 - (height1 - 50))
        frm.pack()

        lbl = CTkLabel(master=frm, text='Меню', font=('Arial', 30))
        center_lbl = width1 // 2
        lbl.pack(padx=(center_lbl - 235, center_lbl - 295), side=LEFT)

        btn = CTkButton(master=frm, text='\u2699', font=('Arial', 30), width=50)
        btn.pack(side=RIGHT)

    def btn_of_chat(self, window):
        btn = CTkButton(master=window, text='Чаты', font=('Arial', 20))
        btn.pack()

    def btn_of_help(self, window):
        btn2 = CTkButton(master=window)


if __name__ == '__main__':
    root = CTk()
    root.config(bg='#33FF33')
    root.title('Дневник садовода и огородника')
    width1 = know_the_size_of_screen()['width']
    height1 = know_the_size_of_screen()['height']
    print(width1, height1)
    root.geometry(f'{width1}x{height1}+{-10}+{0}')
    main_root = MainPage()
    main_root.title_main(root, width1, height1)
    main_root.btn_of_chat(root)
    root.mainloop()
