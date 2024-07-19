import sys
sys.path.append('.')
from customtkinter import *
from Computer_app.about_computer.size_of_screen import know_the_size_of_screen

def return_to_last_page():
    main_root = MenuOfChats()
    frm = main_root.create_top_of_menu_chat(name_of_window=root, width=width1-2, height=height1-(height1-50))
    frm2 = main_root.create_main_frame(name_of_window=root, width=width1-2, height=height1-50, foreground='#33FF33')
    main_root.place_exit_button(frame=frm)
    main_root.place_name_of_menu(frame=frm)
    main_root.place_adder_button()
    
def new_chat():
    global frm
    global frm2
    frm.destroy()
    frm2.destroy()
    def place_exit_button_when_create_a_chat() -> None:
        btn = CTkButton(master=root, text='←', font=('Arial', 20), width=100, height=47)
        btn.pack(anchor='nw')
    place_exit_button_when_create_a_chat()
    lbl = CTkLabel(master=root, text='Название чата:', font=('Arial', 30), bg_color='#33FF33')
    lbl.pack(anchor='center')
    entr1 = CTkEntry(master=root, font=('Arial', 30), width=200)
    entr1.pack(anchor='center')

    btn2 = CTkButton(master=root, text='Создать чат', font=('Arial', 30), command=return_to_last_page)
    btn2.pack(anchor='se')


class MenuOfChats(CTk):
    def create_top_of_menu_chat(self, name_of_window: str, width: int, height: int) -> CTkFrame:
        frm = CTkFrame(master=name_of_window, border_width=1, height=height, width=width, bg_color='white')
        frm.place(x=1, y=0)
        return frm
    
    def create_main_frame(self, name_of_window: str, width: int, height: int, foreground='white') -> CTkFrame:
        frm2 = CTkFrame(master=name_of_window, border_width=1, height=height, width=width, fg_color=foreground)
        frm2.place(x=1, y=height1-(height1-50))
        return frm2

    def place_exit_button(self, frame) -> None:
        btn = CTkButton(master=frame, text='←', font=('Arial', 20), width=100, height=47)
        btn.pack(side=LEFT, padx=(0, 400))
    
    def place_name_of_menu(self, frame):
        lbl = CTkLabel(master=frame, text='Чаты садоводов и огородников:', font=('Arial', 30))
        lbl.pack(side=TOP, padx=(0, height1-(100 + 400 + lbl.winfo_width())))

    def place_adder_button(self):
        btn2 = CTkButton(master=frm2, text='+', corner_radius=1000, bg_color='#33FF33', font=('Arial', 40), width=3, command=new_chat)
        btn2.place(x=width1-555, y=height1-555)


class Chat():
    def create_top_of_the_chat(self, window, height: int, width: int, foreground: str='white') -> None:
        frm = CTkFrame(master=window, border_width=1, height=height, width=width, fg_color=foreground)
        frm.place(x=0, y=0)
    
    def create_part_with_messages(self, window, height: int, width: int, foreground: str='white') -> None:
        frm = CTkFrame(master=window, border_width=1, height=height, width=width, fg_color=foreground)
        frm.place(x=0, y=0)

    def create_part_with_typing_this_message(self, window, height: int, width: int, foreground: str='white') -> None:
        frm = CTkFrame(master=window, border_width=1, height=height, width=width, fg_color=foreground)
        frm.place(x=0, y=0)


if __name__ == '__main__':
    root = CTk()
    root.config(bg='#33FF33')
    root.title('Дневник садовода и огородника')
    width1 = know_the_size_of_screen()['width']
    height1 = know_the_size_of_screen()['height']
    print(width1, height1)
    root.geometry(f'{width1}x{height1}+{-10}+{0}')
    main_root = MenuOfChats()
    frm = main_root.create_top_of_menu_chat(name_of_window=root, width=width1-2, height=height1-(height1-50))
    frm2 = main_root.create_main_frame(name_of_window=root, width=width1-2, height=height1-50, foreground='#33FF33')
    main_root.place_exit_button(frame=frm)
    main_root.place_name_of_menu(frame=frm)
    main_root.place_adder_button()
    root.mainloop()
