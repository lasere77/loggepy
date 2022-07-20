import logging
import ctypes
import locale
import json
from datetime import datetime
from tkinter import Tk, Frame, Label, Entry, Button, messagebox


try:
    import keyboard
    from dotenv import load_dotenv
except:
    from repaired import repair_libs
    repair_libs()

from guimanager import destroy_gui_delpassword

windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["delpassword"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["delpassword"]

def gui_del_password():
    gui_delpassword = Tk()
    gui_delpassword.title("del password")
    gui_delpassword.iconbitmap("Script/img/index.ico")
    gui_delpassword.config(bg="gray17")
    gui_delpassword.geometry("400x600+850+50")

    frame = Frame(gui_delpassword, bg="gray17")
    frame.pack(expand="YES")

    rule = Label(frame, text=data_text["warning"], bg="gray17", fg="#083def")
    rule.pack()

    # input for name of the password
    choose_ligne = Label(frame, text=data_text['choose_ligne'], bg="gray17", fg="#083def")
    choose_ligne.pack()
    put_ligne_password = Entry(frame, bg="gray17", fg="#083def")
    put_ligne_password.pack()

    def get_ligne_put():
        ligne_password = put_ligne_password.get()
        print(ligne_password)
        del_passeword(ligne_password, gui_delpassword)

    btn_confirm_password = Button(frame, text=data_text["confirmed"], bg="gray17", fg="#083def", command=get_ligne_put)
    btn_confirm_password.pack()

    gui_delpassword.mainloop()

def del_passeword(ligne_password, gui_delpassword):
    ligne_password = int(ligne_password)
    logging.info(f'{datetime.now()} INFO: the user called the function "add_passeword"')
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy\passwords")
    if ligne_password == 0:
        pass
    if messagebox.askyesno(data_text["sure"], f"{data_text['del_password']} {int(ligne_password)} {data_text['del_password2']}"):
        file = open("C:\ProgramData\passworld_loggepy\passwords", "r", encoding="UTF-8")
        lignes = file.readlines()
        file.close()
        lignes[int(ligne_password) - 1] = ""
        file = open("C:\ProgramData\passworld_loggepy\passwords", "w", encoding="UTF-8")
        file.writelines(lignes)
        file.close()
        logging.info(f'{datetime.now()} INFO: the user del ligne {ligne_password}')
        print(f"{data_text['password_has_del']} {ligne_password} {data_text['password_has_del2']} ")
        destroy_gui_delpassword(gui_delpassword)
    else:
        destroy_gui_delpassword(gui_delpassword)