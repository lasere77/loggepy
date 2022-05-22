import io
import os

import keyboard
import requests
import zipfile
from bs4 import BeautifulSoup

from relaunch import restart

get_name = os.getlogin()

IMPORTANT = 0
MAJOR = 1
MINOR = 7

point = "."
URL = "https://github.com/lasere77/loggepy/releases"


def get_update():
    reponse = requests.get(URL)
    print("we are looking if there is an update available, thank you for your attention")
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
            print(f"a new update is available.\nYou are currently on the loggepy version{IMPORTANT}{point}{MAJOR}{point}{MINOR}, and the new version is the {get_important}{point}{get_major}{point}{get_minor}\ndo you want to do this update?(yes/no)")
            while True:
                if keyboard.is_pressed("y"):
                    # télécharger la nouvelle vertion de loggepy grace a une requet html + la désipé
                    r = requests.get(file_zip_url)
                    z = zipfile.ZipFile(io.BytesIO(r.content))
                    z.extractall("C:/Windows/Temp/loggepy_update")
                    #executer l'asssembleur
                    os.chdir(f'C:/Users/{get_name}/AppData/Roaming/loggepy')
                    os.system('update.bat')
                    print("la mise a jour a été faite")
                    restart()
                if keyboard.is_pressed("n"):
                    print("la mise a jour n'a pas été faite")
                    restart()
        elif get_important == IMPORTANT or get_major == MAJOR or get_minor == MINOR:
            print("you already have the latest version of loggepy")
