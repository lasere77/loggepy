import os
import logging
import ctypes
import locale
import json

import time


windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["relaunch"]
except:
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["relaunch"]


def restart():
    logging.info("INFO: the program will restart.")
    print(data_text['stop'])
    time.sleep(2.5)
    os.chdir(r"C:\Program Files (x86)\loggepy")
    os.system("launcher.bat")
    error()


def error():
    logging.error("FATAL: the program had to stop ")
    exit()
