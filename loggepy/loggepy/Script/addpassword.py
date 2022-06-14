import logging
import ctypes
import locale
import json
from datetime import datetime

try:
    from dotenv import load_dotenv
    import os
    import shutil
    import time
except:
    from repaired import repair_libs
    repair_libs()

from relaunch import restart


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


def add_password():
    logging.info(f'{datetime.now()} INFO: the user called the function "add_passeword"')
    choose_name = input(data_text['choose_name'])
    print(data_text["escape"])
    choose_addPassword = input(f"{data_text['choose_addpassword']} {choose_name} : ")
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    file = open("C:\ProgramData\passworld_loggepy\passewords", "a+")
    if choose_name == "escape":
        restart()
    if " " in choose_name or "=" in choose_name:
        print(data_text["no_space"])
        time.sleep(2.5)
        restart()
    if choose_name == "":
        print(data_text["put_arg"])
        time.sleep(2.5)
        restart()
    file.write(choose_name + "=" + choose_addPassword)
    file.write("\n")
    print(f"{data_text['saved_passeword']} {choose_name} {data_text['saved_passeword2']} {choose_addPassword} .")
    file.close()
    logging.info(f"{datetime.now()} INFO: the \"backup\" function was called")
    src = r"C:\ProgramData\passworld_loggepy\passewords"
    backup_passeword = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy\passewords_back"
    shutil.copy(src, backup_passeword)
    restart()
