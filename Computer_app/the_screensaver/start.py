import sys
sys.path.append('.')
from tkinter import *
from Computer_app.about_computer.size_of_screen import know_the_size_of_screen
import time

width = know_the_size_of_screen()['width']
height = know_the_size_of_screen()['height']

root = Tk()
root.wm_attributes("-topmost", 1)
root.resizable(width=False, height=False)
root.overrideredirect(1)
window_width = 900
window_height = 500
x = int(int(root.winfo_screenwidth() / 2) - int(window_width / 2))
y = int(int(root.winfo_screenheight() / 2) - int(window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root['bg'] = '#7F00FF'

lbl = Label(root, text='Дневник садовода\nи огородника', font='Arial 40', fg='#33FF33', bg='#7F00FF')
lbl.place(x=150, y=200)

def lbl2_com():
    global lbl2
    global x1
    global y1
    x1 += 1
    lbl2.place(x=x1, y=y1)

def lbl3_com():
    global lbl3
    global x2
    global y2
    x2 += 1
    lbl3.place(x=x2, y=y2)


lbl2 = Label(root, text=' ' * 30, font='Arial 40', fg='#7FFF00', bg='#7F00FF')
x1 = 160
y1 = 200
lbl2.place(x=x1, y=y1)

lbl3 = Label(root, text=' ' * 22, font='Arial 40', fg='#7FFF00', bg='#7F00FF')
x2 = 230
y2 = 270
lbl3.place(x=x2, y=y2)

for i in range(570):
    root.after(1, lbl2_com)
    root.update()
    time.sleep(0.01)
for i in range(420):
    root.after(1, lbl3_com)
    root.update()
    time.sleep(0.01)

time.sleep(2)
root.destroy()


root.mainloop()