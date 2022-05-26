import io
import os
import ctypes
import locale
import json

import keyboard
import requests
import zipfile
from bs4 import BeautifulSoup

from relaunch import restart

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
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["update"]

get_name = os.getlogin()

point = "."
URL = "https://github.com/lasere77/loggepy/releases"


def get_update():
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
            while True:
                if keyboard.is_pressed("y"):
                    # télécharger la nouvelle vertion de loggepy grace a une requet html + la désipé
                    r = requests.get(file_zip_url)
                    z = zipfile.ZipFile(io.BytesIO(r.content))
                    z.extractall("C:/Windows/Temp/loggepy_update")
                    #executer l'asssembleur
                    os.chdir(f'C:/Users/{get_name}/AppData/Roaming/loggepy')
                    os.system('update.bat')
                    print(data_text['ready_update'])
                    restart()
                if keyboard.is_pressed("n"):
                    print(data_text['no_update'])
                    restart()
        elif get_important == IMPORTANT or get_major == MAJOR or get_minor == MINOR:
            print(data_text['last_version'])
