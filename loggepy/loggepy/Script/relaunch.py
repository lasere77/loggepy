import os
import logging
import ctypes
import locale
import json
from datetime import datetime

try:
    import time
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
    data_text = data_texte["relaunch"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["relaunch"]


def restart():
    logging.info(f"{datetime.now()} INFO: the program will restart.")
    print(data_text['stop'])
    time.sleep(2.5)
    os.chdir(r"C:\Program Files (x86)\loggepy")
    os.system("launcher.bat")
    error()


def error():
    logging.error(f"{datetime.now()} FATAL: the program had to stop ")
    exit()
