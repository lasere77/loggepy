import io
import os
import ctypes
import locale
import json
from datetime import datetime
import logging
from tkinter import Tk, Frame, Label, messagebox, Button
import webbrowser
import functools

try:
    import keyboard
    import requests
    import zipfile
    from bs4 import BeautifulSoup
except:
    from repaired import repair_libs
    repair_libs()

from guimanager import destroy_gui_get_update

with open(f"Script/data/data.json", "r") as file:
    data = json.load(file)

MAJOR = int(data["MAJOR"])
MINOR = int(data["MINOR"])
PATCH = int(data["PATCH"])

windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["update"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["update"]

get_name = os.getlogin()

point = "."
URL = "https://github.com/lasere77/loggepy/releases"

def gui_error_update():
    gui_error_update = Tk()
    gui_error_update.title("update error")
    gui_error_update.iconbitmap("Script/img/index.ico")
    gui_error_update.config(bg="gray17")
    width = gui_error_update.winfo_screenwidth()
    height = gui_error_update.winfo_screenheight()
    gui_error_update.geometry("%dx%d" % (width, height))

    frame = Frame(gui_error_update, bg="gray17")
    frame.pack(expand="YES")

    rule = Label(frame, text=data_text['error'], bg="gray17", fg="#083def")
    rule.pack()

    btn = Button(frame, text=data_text['here'], bg="gray17", fg="#083def", command=open_github)
    btn.pack()

    gui_error_update.mainloop()

def open_github():
    webbrowser.open_new("https://github.com/lasere77/loggepy/releases")


def gui_get_update():
    gui_getupdate = Tk()
    gui_getupdate.title("update")
    gui_getupdate.iconbitmap("Script/img/index.ico")
    gui_getupdate.config(bg="gray17")
    width = gui_getupdate.winfo_screenwidth()
    height = gui_getupdate.winfo_screenheight()
    gui_getupdate.geometry("%dx%d" % (width, height))

    frame = Frame(gui_getupdate, bg="gray17")
    frame.pack(expand="YES")

    rule = Label(frame, text=data_text['warning'], bg="gray17", fg="#083def")
    rule.pack()

    get_update(gui_getupdate, frame)

    gui_getupdate.mainloop()

def get_update(gui_getupdate, frame):
    reponse = requests.get(URL)
    print(data_text['looking'])
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        tag = soup.find(name="h1")
        tag.text.replace(".", ",")
        tag = tuple(tag.text)
        print(tag)
        get_major = int(tag[0])
        get_minor_tuple = int(tag[2]), int(tag[3])
        get_minor = functools.reduce(lambda sub, ele: sub * 10 + ele, get_minor_tuple)
        print(type(get_minor))
        print(get_minor)
        get_patch = int(tag[5])

        file_zip_url = f"https://github.com/lasere77/loggepy/releases/download/{get_major}{point}{get_minor}{point}{get_patch}/loggepy.{get_major}{point}{get_minor}{point}{get_patch}.zip"

        if get_major > MAJOR or get_minor > MINOR or get_patch > PATCH:
            print(f"{data_text['new']}\n{data_text['current_version']} {MAJOR}{point}{MINOR}{point}{PATCH} {data_text['new_version']} {get_major}{point}{get_minor}{point}{get_patch}\n{data_text['choose']}")
            desciption = soup.find(name="p")
            if "$" in str(desciption):
                gui_error_update()
            def update():
                if messagebox.askyesno(data_text["title"], f"{data_text['new']}{data_text['current_version']} {MAJOR}{point}{MINOR}{point}{PATCH}\n{data_text['new_version']} {get_major}{point}{get_minor}{point}{get_patch}\n{data_text['choose']}"):
                    # télécharger la nouvelle vertion de loggepy grace a une requet html + la désipé
                    print(data_text["download"])
                    r = requests.get(file_zip_url)
                    z = zipfile.ZipFile(io.BytesIO(r.content))
                    z.extractall("C:/Windows/Temp/loggepy_update")
                    print(data_text['ready_update'])
                    #executer l'asssembleur
                    try:
                        path = f'C:/Users/{get_name}/AppData/Roaming/loggepy/update.bat'
                        os.execl(path, path)
                    except:
                        logging.error(f"{datetime.now()} ERROR: you can no longer update please go to: https://github.com/lasere77/loggepy/releases ")
                        print("ERROR: you can no longer update please go to: https://github.com/lasere77/loggepy/releases")
                        gui_error_update()
                    destroy_gui_get_update(gui_getupdate)
                else:
                    print(data_text['no_update'])
                    destroy_gui_get_update(gui_getupdate)
            print(desciption)
            info = Label(frame, text=str(desciption), bg="gray17", fg="#083def")
            info.pack()
            btn = Button(frame, text=data_text["confirmed"], bg="gray17", fg="#083def", command=update)
            btn.pack()
        elif get_major == get_major or get_minor == MINOR or get_patch == PATCH:
            last = Label(frame, text=data_text['last_version'], bg="gray17", fg="#083def")
            last.pack()
            print(data_text['last_version'])