import os
import shutil
import logging
import ctypes
import locale
import json


windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["repaired"]
except:
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_texte = data["text"]
    data_text = data_texte["repaired"]

def repair():
    logging.info("INFO: the \"repair\" function was called")
    backup_file_passewords = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy"
    passewords_file = r"C:\ProgramData\passworld_loggepy\passewords"
    shutil.copy(backup_file_passewords, passewords_file)
    print(data_text['repair_succes'])

