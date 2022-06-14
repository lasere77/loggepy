import logging
import os
import ctypes
import locale
import json
from datetime import datetime

try:
    from dotenv import load_dotenv
    import pyperclip as pc
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
    data_text = data_texte["getpassword"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["getpassword"]


def get_passeword():
    logging.info(f'{datetime.now()} INFO: the user called the function "get_passeword"')
    print(data_text["escape"])
    choose = input(data_text["choose"])
    if choose == "escape":
        restart()
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    print(os.getenv(choose))


def get_all_passeword():
    logging.info(f'{datetime.now()} INFO: the user called the function "all_passeword"')
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    file = open("C:\ProgramData\passworld_loggepy\passewords", "r")
    print(data_text['all_password'])
    print("\n" + file.read())


def copy():
    logging.info(f'{datetime.now()} INFO: the user called the function "copy"')
    choose = input(data_text['choose_copy'])
    if choose == "escape":
        restart()
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    print(os.getenv(choose) , data_text['copyed'])
    pc.copy(os.getenv(choose))
