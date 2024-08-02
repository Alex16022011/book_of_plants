import sys
sys.path.append('.')
from customtkinter import CTk, END, CTkButton, CTkTextbox, CENTER, LEFT, SE, RIGHT, CTkFont, DISABLED
from Computer_app.about_computer.size_of_screen import know_the_size_of_screen as sizes
from classes_of_programm.remove_all_objects_from_screen import destroy_all_from_screen
from CTkListbox import *
from threading import *
import socket
from chat_for_app.user import sending

host = socket.gethostbyname(socket.gethostname())
port = 0
server = (socket.gethostbyname(socket.gethostname()), 51245)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
username = 'Ира'
s.sendto((f'@ {username} : join chat \n').encode("utf-8"), server)

def receving(s, list_field):
    while True:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            list_field.insert(END, data)
            print('Вставил дата')
            # if 'https://www.' in data:
            #     if yes_no := True:
            #         webbrowser.open(data[data.index('[') + 1:data.index(']')])
        except:
            pass


def main_programm():
    global text_box


    def split_message(message: str, step: int, sep: str='', join: bool=False) -> str:
        if 0 < step <= len(message):
            if join:
                new_message = ''
                step2 = 0
                while step2 + step <= len(message):
                    new_message += f'{message[step2 : step2 + step]}{sep}'
                    step2 += step
                return new_message
            else:
                new_message = []
                step2 = 0
                while step2 + step <= len(message):
                    new_message.append(f'{message[step2 : step2 + step]}{sep}')
                    step2 += step
                return new_message
        return message

    def send_and_get_messages():
        global text_box
        message = text_box.get('0.0', END)
        thr2 = Thread(target=sending, args=(message, 'Петя', s, server, listbox))
        thr2.daemon = True
        thr2.start()
        thr2.join()
        if message.strip() != '':
            # message = split_message(message, step=28, join=False)
            # listbox.insert(END, f'@ Я : {message[0]}')
            # indent = 6
            # for i in range(len(message[1:])):
            #     listbox.insert(END, indent * ' ' + message[i])
            listbox.insert(END, f'{message}, {len(message)}')
        thr3 = Thread(target=receving, args=(s, listbox))
        thr3.daemon = True
        thr3.start()
        text_box.delete('0.0', END)


    root = CTk()
    h = sizes()['height'] - 70
    w = sizes()['width'] + 1
    root.geometry(f'{w}x{h}+{-10}+0')
    root.resizable(0, 0)

    font_for_listbox = CTkFont(family = 'Arial', size=25, weight='normal', slant='roman')

    listbox = CTkListbox(root, fg_color='#00FF00', font=font_for_listbox)
    listbox.pack(fill="both", expand=True, padx=10, pady=10)

    text_box = CTkTextbox(master=root, font=('Arial', 20), bg_color='black', fg_color='white', height=70, width=(w - 131), border_color='black', border_width=2)
    text_box.event_add('<<Paste>>', '<Control-igrave>')
    # text_box.configure(state=DISABLED)
    text_box.event_add("<<Copy>>", "<Control-ntilde>")
    text_box.pack(side=LEFT, anchor=CENTER, padx=(10, 10), pady=(0, 10))
    btn_send = CTkButton(master=root, text='➤', fg_color='#3399FF', text_color='white', font=('Arial', 30), height=50, width=20, corner_radius=1000, command=send_and_get_messages)
    btn_send.pack(side=RIGHT, anchor=SE, padx=(10, 20), pady=(0, 20))

    root.mainloop()


thr1 = Thread(target=main_programm)
thr1.daemon = True
thr1.start()
thr1.join()