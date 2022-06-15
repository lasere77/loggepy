import logging
import ctypes
import locale
import json
import time
from datetime import datetime
try:
    import keyboard
    from dotenv import load_dotenv
    from relaunch import restart
    from getpasseword import get_all_passeword
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
    data_text = data_texte["delpassword"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["delpassword"]


def del_passeword():
    logging.info(f'{datetime.now()} INFO: the user called the function "add_passeword"')
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    get_all_passeword()
    print(data_text["escape"])
    choose_ligne = input(data_text['choose_ligne'])
    if choose_ligne == "escape" or choose_ligne == 0:
        restart()
    try:
        int(choose_ligne)
    except:
        print(data_text["put_int"])
        time.sleep(2)
        del_passeword()
    try:
        file = open("C:\ProgramData\passworld_loggepy\passewords", "r")
        file.close()
        print(f"{data_text['del_password']} {int(choose_ligne)} {data_text['del_password2']}")
        while True:
            if keyboard.is_pressed("y"):
                file = open("C:\ProgramData\passworld_loggepy\passewords", "r")
                lignes = file.readlines()
                file.close()
                lignes[int(choose_ligne) - 1] = ""
                file = open("C:\ProgramData\passworld_loggepy\passewords", "w")
                file.writelines(lignes)
                file.close()
                logging.info(f'{datetime.now()} INFO: the user del ligne {choose_ligne}')
                print(f"{data_text['password_has_del']} {choose_ligne} {data_text['password_has_del2']} ")
                restart()
            elif keyboard.is_pressed("n"):
                restart()
    except:
        restart()

