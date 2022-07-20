import logging
import os
import ctypes
import locale
import json
from datetime import datetime
from tkinter import Tk, Label, Frame, Button, Entry

try:
    from dotenv import load_dotenv
    import pyperclip as pc
except:
    from repaired import repair_libs
    repair_libs()

windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["getpassword"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["getpassword"]


def gui_getpassword():
    gui_getpassword = Tk()
    gui_getpassword.title("get password")
    gui_getpassword.iconbitmap("Script/img/index.ico")
    gui_getpassword.config(bg="gray17")
    gui_getpassword.geometry("400x600+850+50")

    frame = Frame(gui_getpassword, bg="gray17")
    frame.pack(expand="YES")

    rule = Label(frame, text=data_text["warning"], bg="gray17", fg="#083def")
    rule.pack()

    # input for name of the password
    choose_name = Label(frame, text=data_text["choose"], bg="gray17", fg="#083def")
    choose_name.pack()
    put_name_password = Entry(frame, bg="gray17", fg="#083def")
    put_name_password.pack()

    def get_name_password_put():
        name_password = put_name_password.get()
        print(name_password)
        get_passeword(name_password, frame)

    btn_confirm_password = Button(frame, text=data_text["confirmed"], bg="gray17", fg="#083def", command=get_name_password_put)
    btn_confirm_password.pack()

    gui_getpassword.mainloop()

def get_passeword(name_password, frame):
    name_password = str(name_password)
    logging.info(f'{datetime.now()} INFO: the user called the function "get_passeword"')
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy\passwords")
    password = Label(frame, text=data_text["your_password"] + os.getenv(name_password), bg="gray17", fg="#083def")
    password.pack()
    print(os.getenv(name_password))


def gui_getallpassword():
    gui_getallpassword = Tk()
    gui_getallpassword.title("get all password")
    gui_getallpassword.iconbitmap("Script/img/index.ico")
    gui_getallpassword.config(bg="gray17")
    gui_getallpassword.geometry("400x600+850+50")

    frame = Frame(gui_getallpassword, bg="gray17")
    frame.pack(expand="YES")

    get_all_passeword(frame)

    gui_getallpassword.mainloop()

def get_all_passeword(frame):
    logging.info(f'{datetime.now()} INFO: the user called the function "all_passeword"')
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy\passwords")
    file = open("C:\ProgramData\passworld_loggepy\passwords", "r", encoding="UTF-8")
    all_password = Label(frame, text=data_text['all_password'] + "\n" + file.read(), bg="gray17", fg="#083def")
    all_password.pack()
    print(data_text['all_password'])
    print("\n" + file.read())


def gui_copy_password():
    gui_getallpassword = Tk()
    gui_getallpassword.title("copy password")
    gui_getallpassword.iconbitmap("Script/img/index.ico")
    gui_getallpassword.config(bg="gray17")
    gui_getallpassword.geometry("400x600+850+50")

    frame = Frame(gui_getallpassword, bg="gray17")
    frame.pack(expand="YES")

    choose_password = Label(frame, text=data_text['choose_copy'], bg="gray17", fg="#083def")
    choose_password.pack()
    put_name_password = Entry(frame, bg="gray17", fg="#083def")
    put_name_password.pack()

    def get_copy_password_put():
        name_password = put_name_password.get()
        print(name_password)
        copy(name_password, frame)

    btn_confirm_password = Button(frame, text=data_text["confirmed"], bg="gray17", fg="#083def", command=get_copy_password_put)
    btn_confirm_password.pack()

    gui_getallpassword.mainloop()

def copy(name_password, frame):
    name_password = str(name_password)
    logging.info(f'{datetime.now()} INFO: the user called the function "copy"')
    try:
        password_copyed = Label(frame, text=os.getenv(name_password) + data_text['copyed'], bg="gray17", fg="#083def")
        password_copyed.pack()
        load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy\passwords")
        print(os.getenv(name_password), data_text['copyed'])
        pc.copy(os.getenv(name_password))
    except:
        password_not_copyed = Label(frame, text=data_text["not_copyed"], bg="gray17", fg="#083def")
        password_not_copyed.pack()
