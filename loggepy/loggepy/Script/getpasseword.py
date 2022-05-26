import logging
import os
import ctypes
import locale
import json

from dotenv import load_dotenv
import pyperclip as pc

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
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["getpassword"]


def get_passeword():
    logging.info('INFO: the user called the function "get_passeword"')
    print(data_text["escape"])
    choose = input(data_text["choose"])
    if choose == "escape":
        restart()
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    print(os.getenv(choose))


def get_all_passeword():
    logging.info('INFO: the user called the function "all_passeword"')
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    file = open("C:\ProgramData\passworld_loggepy\passewords", "r")
    print(data_text['all_password'])
    print("\n" + file.read())


def copy():
    logging.info('INFO: the user called the function "copy"')
    choose = input(data_text['choose_copy'])
    if choose == "escape":
        restart()
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    print(os.getenv(choose) , data_text['copyed'])
    pc.copy(os.getenv(choose))
