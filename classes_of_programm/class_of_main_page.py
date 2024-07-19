from customtkinter import *

class MainPage():
    def btn_of_chat(self, window):
        btn = CTkButton(master=window)

    def btn_of_help(self, window):
        btn2 = CTkButton(master=window)    

if __name__ == '__main__':
    root = CTk()
    main_root = MainPage()
    main_root.btn_of_chat(root)
    root.mainloop()