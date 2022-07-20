import logging
import ctypes
import locale
import json
from datetime import datetime
from tkinter import Tk, Label, Frame, Entry, Button

try:
    from dotenv import load_dotenv
    import os
    import shutil
    import time
except:
    from repaired import repair_libs
    repair_libs()

from guimanager import destroy_gui_addpassword

windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["addpassword"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["addpassword"]

def gui_add_password():
    gui_addpassword = Tk()
    gui_addpassword.title("add password")
    gui_addpassword.iconbitmap("Script/img/index.ico")
    gui_addpassword.config(bg="gray17")
    gui_addpassword.geometry("400x600+850+50")

    frame = Frame(gui_addpassword, bg="gray17")
    frame.pack(expand="YES")

    rule = Label(frame, text=data_text["warning"], bg="gray17", fg="#083def")
    rule.pack()

    # input for name of the password
    choose_name = Label(frame, text=data_text["choose_name"], bg="gray17", fg="#083def")
    choose_name.pack()
    put_name_password = Entry(frame, bg="gray17", fg="#083def")
    put_name_password.pack()

    def get_password_put():
        name_password = put_name_password.get()
        print(name_password)
        password = put_password.get()
        print(password)
        add_password(name_password, password, gui_addpassword)

    choose_password = Label(frame, text=data_text["choose_addpassword"], bg="gray17", fg="#083def")
    choose_password.pack()
    put_password = Entry(frame, bg="gray17", fg="#083def")
    put_password.pack()

    btn_confirm_password = Button(frame, text=data_text["confirmed"], bg="gray17", fg="#083def", command=get_password_put)
    btn_confirm_password.pack()

    gui_addpassword.mainloop()


def add_password(name_password, password, gui_addpassword):
    name_password = str(name_password)
    password = str(password)
    logging.info(f'{datetime.now()} INFO: the user called the function "add_passeword"')
    if " " in name_password or "=" in name_password:
        print(data_text["no_space"])
        time.sleep(2.5)
    if name_password == "":
        print(data_text["put_arg"])
        time.sleep(2.5)
    if "=" in password or password == " ":
        print(data_text["no_equals"])
        time.sleep(2.5)
    if password == "":
        print(data_text["put_arg"])
        time.sleep(2.5)
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passwords")
    file = open("C:\ProgramData\passworld_loggepy\passwords", "a+", encoding="UTF-8")
    print(password)
    file.write(name_password + "=" + password)
    file.write("\n")
    file.close()
    logging.info(f"{datetime.now()} INFO: the \"backup\" function was called")
    src = r"C:\ProgramData\passworld_loggepy\passwords"
    backup_passeword = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy\passewords_back"
    shutil.copy(src, backup_passeword)
    destroy_gui_addpassword(gui_addpassword)
