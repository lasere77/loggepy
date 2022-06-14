import random
import logging
import string
import shutil
import os
import ctypes
import locale
import json
from datetime import datetime

try:
    from pyfade import Colors, Fade
    import keyboard
    import time
except:
    from repaired import repair_libs
    repair_libs()

from getpasseword import get_passeword, get_all_passeword, copy
from addpassword import add_password
from relaunch import restart
from repaired import repair
from delpassewod import del_passeword
from update import get_update

logging.basicConfig(filename="log/loggepy_log.log", level=logging.DEBUG)

with open(f"Script/data/data.json", "r") as file:
    data = json.load(file)

thank = """
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

██╗░░░██╗░██████╗██╗███╗░░██╗░██████╗░  ██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░██╗░░░██╗
██║░░░██║██╔════╝██║████╗░██║██╔════╝░  ██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗╚██╗░██╔╝
██║░░░██║╚█████╗░██║██╔██╗██║██║░░██╗░  ██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝░╚████╔╝░
██║░░░██║░╚═══██╗██║██║╚████║██║░░╚██╗  ██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔═══╝░░░╚██╔╝░░
╚██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░░░░░░░██║░░░
░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░
"""
title = f"""
██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░██╗░░░██╗ {data["version"]}
██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗╚██╗░██╔╝ by {data["author"]}
██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝░╚████╔╝░
██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔═══╝░░░╚██╔╝░░
███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░░░░░░░██║░░░
╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░ 
"""
#get the language
windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

try:
    with open(f"Script/LANG/{lang}.json", "r") as f:
        data = json.load(f)
    data_litel = data["litel"]
    data_big = data["big"]
    data_texte = data["text"]
    data_text = data_texte["loggepy"]
except:
    logging.error(f"{datetime.now()} ERROR: no language file corresponds to that of your computer, the language will be English")
    with open(f"Script/LANG/en_US.json", "r") as f:
        data = json.load(f)
    data_litel = data["litel"]
    data_big = data["big"]
    data_texte = data["text"]
    data_text = data_texte["loggepy"]

print(Fade.Vertical(Colors.blue_to_green, title))
hm = list(string.ascii_lowercase + "\"" + "@" + "<")
HM = list(string.ascii_uppercase + "/" + "*" + ">" + "~")
file = open("C:\ProgramData\passworld_loggepy\passewords", "a+")
print(f'{data_litel["generate"]}\n{data_litel["read"]}\n{data_litel["creata"]}\n{data_litel["exit"]}\n{data_litel["see"]}\n{data_litel["copy"]}\n{data_litel["backup"]} \n{data_litel["delete"]}\n{data_litel["info"]} \n{data_litel["update"]}')


def passeword_generet():
    logging.info(f"{datetime.now()} INFO: the user called the function \"passeword_generet\"")
    print(data_text["escape"])
    name_passewod = input(data_text['name_passewod'])
    if name_passewod == "escape":
        restart()
    if " " in name_passewod or "=" in name_passewod:
        print(data_text['no_space'])
        time.sleep(2.5)
        restart()
    file.write(name_passewod + "=")
    for i in range(12):
        passeword = (hm[random.randint(0, len(hm) - 1)] + HM[random.randint(0, len(hm) - 1)])
        file.write(str(passeword))
    file.write("\n")
    print(data_text['register'], name_passewod)
    file.close()
    logging.info(f"{datetime.now()} INFO: the \"backup\" function was called")
    src = r"C:\ProgramData\passworld_loggepy\passewords"
    backup_passeword = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy\passewords_back"
    shutil.copy(src, backup_passeword)
    restart()


while True:
    if keyboard.is_pressed("w"):
        logging.info(f"{datetime.now()} INFO: user to press \"w\"")
        logging.info(f"{datetime.now()} INFO: the user called the function \"passeword_generet\" in this path \"C:\Program Files (x86)\loggepy\Script/loggepy.py\" ")
        passeword_generet()

    if keyboard.is_pressed("r"):
        logging.info(f"{datetime.now()} INFO: user to press \"r\"")
        logging.info(f"{datetime.now()} INFO: the user called the function \"get_passeword\" in this path \"C:\Program Files (x86)\loggepy\Script/getpasseword.py\" ")
        get_passeword()

    if keyboard.is_pressed("a"):
        logging.info(f"{datetime.now()} INFO: user to press \"a\"")
        logging.info(f"{datetime.now()} INFO: the user called the function \"add_password\" in this path \"C:\Program Files (x86)\loggepy\Script/addpassword.py\" ")
        add_password()

    if keyboard.is_pressed("e"):
        logging.info(f"{datetime.now()} INFO: user to press \"e\"")
        print(Fade.Vertical(Colors.blue_to_green, thank))
        time.sleep(3)
        exit()

    if keyboard.is_pressed("p"):
        logging.info(f"{datetime.now()} INFO: user to press \"p\"")
        logging.info(f"{datetime.now()} INFO: the user called the function \"all_passeword\" in this path \"C:\Program Files (x86)\loggepy\Script/getpasseword.py\" ")
        get_all_passeword()
        time.sleep(1.5)

    if keyboard.is_pressed("c"):
        logging.info(f"{datetime.now()} INFO: user to press \"c\"")
        logging.info(f"{datetime.now()} INFO: the user called the function \"copy\" in this path \"C:\Program Files (x86)\loggepy\Script/getpasseword.py\" ")
        copy()

    if keyboard.is_pressed("b"):
        logging.info(f"{datetime.now()} INFO: user to press \"b\"")
        logging.info(f"{datetime.now()} INFO: the user called the function \"repair\" in this path \"C:\Program Files (x86)\loggepy\Script/repaired.py\" ")
        repair()
        time.sleep(1.5)

    if keyboard.is_pressed("i"):
        logging.info(f"{datetime.now()} INFO: user to press \"i\"")
        logging.info(f"{datetime.now()} INFO: user requested more info ")
        print(f'\n{data_big["b_generate"]}\n{data_big["b_read"]}\n{data_big["b_creata"]}\n{data_big["b_exit"]}\n{data_big["b_see"]}\n{data_big["b_copy"]}\n{data_big["b_backup"]} \n{data_big["b_delete"]}\n{data_big["b_update"]}')
        time.sleep(2.5)

    if keyboard.is_pressed("d"):
        logging.info(f"{datetime.now()} INFO: user to press \"d\"")
        logging.info(f"{datetime.now()} INFO: the user called the function \"del_passeword\" in this path \"C:\Program Files (x86)\loggepy\Script/delpasseword.py\" ")
        del_passeword()

    if keyboard.is_pressed("u"):
        logging.info(f"{datetime.now()} INFO: user to press \"u\"")
        logging.info(f"{datetime.now()} INFO: the user called the function \"get_update\" in this path \"C:\Program Files (x86)\loggepy\Script/update.py\"")
        get_update()
        time.sleep(3)
# mettre un mot de passe pour voir l'ensemble des nom de mot de passe a faire a la toute fin du project
