import sys
sys.path.append('.')
import socket
from customtkinter import END
# import webbrowser
def sending(username, message, s, server, list_field):
    try:
        if message != '':
            s.sendto((f'@ {username} : {message} \n').encode('utf-8'), server)
    except:
        s.sendto((f'@ {username} : left chat \n').encode("utf-8"), server)
    print('Отправил сообщение')