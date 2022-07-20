import random
import logging
import string
import shutil
import os
import ctypes
import locale
import json
from datetime import datetime
from tkinter import *

try:
    from pyfade import Colors, Fade
    import keyboard
    import time
except:
    from repaired import repair_libs
    repair_libs()

from getpasseword import gui_getpassword, gui_getallpassword, gui_copy_password
from addpassword import gui_add_password
from repaired import repair, gui_uninstall
from delpassewod import gui_del_password
from update import gui_get_update
from guimanager import destroy_gui_passwordgeneret

logging.basicConfig(filename="log/loggepy_log.log", level=logging.DEBUG)

with open(f"Script/data/data.json", "r") as file:
    data = json.load(file)

thank = """
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░██████╗██╗███╗░░██╗░██████╗░  ██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░██╗░░░██╗
██║░░░██║██╔════╝██║████╗░██║██╔════╝░  ██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗╚██╗░██╔╝
██║░░░██║╚█████╗░██║██╔██╗██║██║░░██╗░  ██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝░╚████╔╝░
██║░░░██║░╚═══██╗██║██║╚████║██║░░╚██╗  ██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔═══╝░░░╚██╔╝░░
╚██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░░░░░░░██║░░░
░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░
"""
title = f"""
██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░██╗░░░██╗ {data["version"]}
██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗╚██╗░██╔╝ by {data["author"]}
██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝░╚████╔╝░
██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔═══╝░░░╚██╔╝░░
███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░░░░░░░██║░░░
╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░ 
"""
#get the language
windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data_lang = json.load(f)
    data_litel = data_lang["litel"]
    data_big = data_lang["big"]
    data_texte = data_lang["text"]
    data_text = data_texte["loggepy"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_litel = data["litel"]
    data_big = data["big"]
    data_texte = data["text"]
    data_text = data_texte["loggepy"]


print(Fade.Vertical(Colors.blue_to_green, title))
loggepy_commands = f'\n{data_big["b_generate"]}\n{data_big["b_read"]}\n{data_big["b_creata"]}\n{data_big["b_exit"]}\n{data_big["b_see"]}\n{data_big["b_copy"]}\n{data_big["b_backup"]} \n{data_big["b_delete"]}\n{data_big["b_update"]}'
hm = list(string.ascii_lowercase + "\"" + "@" + "<")
HM = list(string.ascii_uppercase + "/" + "*" + ">" + "~")
#print(f'{data_litel["generate"]}\n{data_litel["read"]}\n{data_litel["creata"]}\n{data_litel["exit"]}\n{data_litel["see"]}\n{data_litel["copy"]}\n{data_litel["backup"]} \n{data_litel["delete"]}\n{data_litel["info"]} \n{data_litel["update"]}')

def gui_passeword_generet():
    gui_passewordgeneret = Tk()
    gui_passewordgeneret.title("passeword generet")
    gui_passewordgeneret.iconbitmap("Script/img/index.ico")
    gui_passewordgeneret.config(bg="gray17")
    gui_passewordgeneret.geometry("400x600+850+50")

    frame = Frame(gui_passewordgeneret, bg="gray17")
    frame.pack(expand="YES")

    rule = Label(frame, text=data_text["warning"], bg="gray17", fg="#083def")
    rule.pack()

    # input for name of the password
    choose_name = Label(frame, text=data_text['name_passewod'], bg="gray17", fg="#083def")
    choose_name.pack()
    put_name_password = Entry(frame, bg="gray17", fg="#083def")
    put_name_password.pack()

    def get_name_password_put():
        name_password = put_name_password.get()
        print(name_password)
        passeword_generet(name_password, gui_passewordgeneret)

    btn_confirm_password = Button(frame, text=data_text["confirmed"], bg="gray17", fg="#083def", command=get_name_password_put)
    btn_confirm_password.pack()

    gui_passewordgeneret.mainloop()


def passeword_generet(name_password, gui_passewordgeneret):
    name_password = str(name_password)
    file = open("C:\ProgramData\passworld_loggepy\passwords", "a+", encoding="UTF-8")
    logging.info(f"{datetime.now()} INFO: the user called the function \"passeword_generet\"")
    if " " in name_password or "=" in name_password:
        print(data_text['no_space'])
        time.sleep(2.5)
    if name_password == "":
        print(data_text['put_arg'])
        time.sleep(2.5)
    file.write(name_password + "=")
    for i in range(12):
        passeword = (hm[random.randint(0, len(hm) - 1)] + HM[random.randint(0, len(hm) - 1)])
        file.write(str(passeword))
    file.write("\n")
    print(data_text['register'], name_password)
    file.close()
    logging.info(f"{datetime.now()} INFO: the \"backup\" function was called")
    src = r"C:\ProgramData\passworld_loggepy\passwords"
    backup_passeword = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy\passewords_back"
    shutil.copy(src, backup_passeword)
    destroy_gui_passwordgeneret(gui_passewordgeneret)

def gui_loggepy_help():
    gui_help = Tk()
    gui_help.title("help")
    gui_help.iconbitmap("Script/img/index.ico")
    gui_help.config(bg="gray17")
    width = gui_help.winfo_screenwidth()
    height = gui_help.winfo_screenheight()
    gui_help.geometry("%dx%d" % (width, height))
    frame = Frame(gui_help, bg="gray17")
    frame.pack(expand="YES")

    # input for name of the password
    choose_name = Label(frame, text=loggepy_commands, bg="gray17", fg="#083def")
    choose_name.pack()
    print(loggepy_commands)
    gui_help.mainloop()


color = {"greys": "#252726", "blue": "#083def", "burgundy": "#6d0c0c"}

gui = Tk()
gui.title("Loggepy")
gui.iconbitmap("Script/img/index.ico")
gui.config(bg="gray17")
gui.geometry("400x600+850+50")

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="Script/img/menu.png")
closeIcon = PhotoImage(file="Script/img/close.png")


def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navgui.place(x=-x, y=0)
            topFrame.update()
            bottom_frame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="blue")
        author_label.config(bg=color["blue"])
        topFrame.config(bg=color["blue"])
        gui.config(bg="gray17")

        #bottom
        bottom_frame.config(bg=color["blue"])

        # turning button OFF:
        btnState = False
    else:
        # make gui dim:
        brandLabel.config(bg=color["greys"], fg="blue")
        author_label.config(bg=color["blue"])
        topFrame.config(bg=color["greys"])
        gui.config(bg=color["greys"])

        #bottom
        bottom_frame.config(bg=color["greys"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navgui.place(x=x, y=0)
            topFrame.update()
            bottom_frame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = Frame(gui, bg=color["blue"])
topFrame.pack(side="top", fill=X)

#bottom frame
bottom_frame = Frame(gui, bg=color["blue"])
bottom_frame.pack(side="bottom", fill=X)

# Header label text:
author_label = Label(topFrame, text="by lasere77", font="Bahnschrift 15", bg=color["blue"], fg="gray17", height=2, padx=20)
author_label.pack(side="right")

# Main label text:
brandLabel = Label(gui, text="Loggepy", font="System 30", bg="gray17", fg="blue")
brandLabel.place(x=100, y=250)

# Label version off loggepy
versionLabel = Label(bottom_frame, text=data["version"], font="Bahnschrift 15", bg=color["blue"], fg="gray17", height=2, padx=20)
versionLabel.pack(expand="Yes")

# Navbar button:
navbarBtn = Button(topFrame, image=navIcon, bg=color["blue"], activebackground=color["blue"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navgui = Frame(gui, bg="gray17", height=1000, width=300)
navgui.place(x=-300, y=0)
Label(navgui, font="Bahnschrift 15", bg=color["blue"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["generet passeword", "get passeword", "add password", "get all passeword", "copy", "repair", "Help", "del passeword", "get update", "exit", "uninstall"]
commands = [gui_passeword_generet, gui_getpassword, gui_add_password, gui_getallpassword, gui_copy_password, repair, gui_loggepy_help, gui_del_password, gui_get_update, exit, gui_uninstall]
# Navbar Option Buttons:
for i in range(len(options)):
    Button(navgui, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["blue"], activebackground="gray17", activeforeground=color["burgundy"], command=commands[i],  bd=0).place(x=25, y=y)
    y += 40

    if i == len(options) - 2:
        y+=80

# Navbar Close Button:
closeBtn = Button(navgui, image=closeIcon, bg=color["blue"], activebackground=color["blue"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

gui.mainloop()

#mettre un mot de passe pour voir l'ensemble des nom de mot de passe a faire a la toute fin du project
#dans le fichier update faire un système qui récupaire le commantaire de la mise a jour et si le commantaire comporte un caractère bien spécial alor cella voudra dire qu'il est risqué de faire la maj et l'utilisateur serra prévenus
    #(encodé le fichier des mot de passe en UTF-8 pour que les caractère spéciaux ne facce pas crash == fait !!!)
    #réglé les problème de droit d'admin ((update == && repaired == fix))
    #kill le gui quand la fonction relaunch est activé (error d'importation circulaire)