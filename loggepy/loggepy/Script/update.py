import io
import os
import ctypes
import locale
import json
from datetime import datetime
import logging
from tkinter import Tk, Frame, Label, messagebox, Button

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

IMPORTANT = int(data["IMPORTANT"])
MAJOR = int(data["MAJOR"])
MINOR = int(data["MINOR"])

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
        get_important = int(tag[0])
        get_major = int(tag[2])
        get_minor = int(tag[4])

        file_zip_url = f"https://github.com/lasere77/loggepy/releases/download/{get_important}{point}{get_major}{point}{get_minor}/loggepy.{get_important}{point}{get_major}{point}{get_minor}.zip"

        if get_important > IMPORTANT or get_major > MAJOR or get_minor > MINOR:
            print(f"{data_text['new']}\n{data_text['current_version']} {IMPORTANT}{point}{MAJOR}{point}{MINOR} {data_text['new_version']} {get_important}{point}{get_major}{point}{get_minor}\n{data_text['choose']}")
            def update():
                if messagebox.askyesno(data_text["title"], f"{data_text['new']}{data_text['current_version']} {IMPORTANT}{point}{MAJOR}{point}{MINOR}\n{data_text['new_version']} {get_important}{point}{get_major}{point}{get_minor}\n{data_text['choose']}"):
                    # télécharger la nouvelle vertion de loggepy grace a une requet html + la désipé
                    print(data_text["download"])
                    r = requests.get(file_zip_url)
                    z = zipfile.ZipFile(io.BytesIO(r.content))
                    z.extractall("C:/Windows/Temp/loggepy_update")
                    print(data_text['ready_update'])
                    #executer l'asssembleur
                    path = f'C:/Users/{get_name}/AppData/Roaming/loggepy/update.bat'
                    os.execl(path, path)
                    destroy_gui_get_update(gui_getupdate)
                else:
                    print(data_text['no_update'])
                    destroy_gui_get_update(gui_getupdate)

            desciption = soup.find(name="p")
            print(desciption)
            info = Label(frame, text=str(desciption), bg="gray17", fg="#083def")
            info.pack()
            btn = Button(frame, text=data_text["confirmed"], bg="gray17", fg="#083def", command=update)
            btn.pack()
        elif get_important == IMPORTANT or get_major == MAJOR or get_minor == MINOR:
            last = Label(frame, text=data_text['last_version'], bg="gray17", fg="#083def")
            last.pack()
            print(data_text['last_version'])