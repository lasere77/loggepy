import os
import shutil
import logging
import ctypes
import locale
import json
from datetime import datetime
from tkinter import Tk, Label, Frame, Button, messagebox


windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["repaired"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["repaired"]


def repair():
    logging.info(f"{datetime.now()} INFO: the \"repair\" function was called")
    backup_file_passewords = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy\passewords_back"
    passewords_file = r"C:\ProgramData\passworld_loggepy\passwords"
    shutil.copy(backup_file_passewords, passewords_file)
    print(data_text['repair_succes'])


def repair_libs():
    #logging.WARN(f"{datetime.now()} WARNING: A library is missing. Attempt to add this library")
    os.chdir(f'C:\Program Files (x86)\loggepy\Script')
    os.system("setup_libs.bat")

def gui_uninstall():
    gui_uninstall = Tk()
    gui_uninstall.title("uninstall")
    gui_uninstall.iconbitmap("Script/img/index.ico")
    gui_uninstall.config(bg="gray17")
    gui_uninstall.geometry("400x600+850+50")

    frame = Frame(gui_uninstall, bg="gray17")
    frame.pack(expand="YES")

    sure = Label(frame, text=data_text["sure"], bg="gray17", fg="#083def")
    sure.pack()

    btn = Button(frame, text=data_text["confirmed"], bg="gray17", fg="#083def", command=uninstall)
    btn.pack()

    gui_uninstall.mainloop()

def uninstall():
    if messagebox.askyesno("uninstall", data_text["to_gods"]):
        logging.info(f"{datetime.now()} INFO: the \"uninstall\" function was called. to gods...")
        os.chdir(f'C:\Program Files (x86)\loggepy')
        os.system("uninstall.bat")
    else:
        exit()