import os
import shutil
import logging
import ctypes
import locale
import json
from datetime import datetime


windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["repaired"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["repaired"]


def repair():
    logging.info(f"{datetime.now()} INFO: the \"repair\" function was called")
    backup_file_passewords = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy"
    passewords_file = r"C:\ProgramData\passworld_loggepy\passewords"
    shutil.copy(backup_file_passewords, passewords_file)
    print(data_text['repair_succes'])


def repair_libs():
    #logging.WARN(f"{datetime.now()} WARNING: A library is missing. Attempt to add this library")
    os.chdir(f'C:\Program Files (x86)\loggepy\Script')
    os.system("setup_libs.bat")