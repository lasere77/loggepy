import random
import logging
import string
import shutil
import os

from pyfade import Colors, Fade
import keyboard
import time

from getpasseword import get_passeword, get_all_passeword, copy
from addpassword import add_password
from relaunch import restart, error
from repaired import repair
from delpassewod import del_passeword
from update import get_update

logging.basicConfig(filename="log/loggepy_log.log", level=logging.DEBUG)
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
title = """
██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░██╗░░░██╗ V 0.1.7
██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗╚██╗░██╔╝ by lasere
██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝░╚████╔╝░
██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔═══╝░░░╚██╔╝░░
███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░░░░░░░██║░░░
╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░ 
"""

print(Fade.Vertical(Colors.blue_to_green, title))
hm = list(string.ascii_lowercase + "\"" + "@" + "<")
HM = list(string.ascii_uppercase + "/" + "*" + ">" + "~")
file = open("C:\ProgramData\passworld_loggepy\passewords", "a+")
print(f'to generate a password press "w" \nto read a password press "r" \nto create a password press "a" \nto exit plesse press "e" \nto see all your passwords press "p" \nto copy your word press "c" \nif your ./passewords file is corrupted colled this function with "b" \nto delete a password press "d" \nto see more details press "i" \nto update loggepy press "u"')


def passeword_generet():
    logging.info("INFO: the user called the function \"passeword_generet\"")
    name_passewod = input("name of new passeword : ")
    if " " in name_passewod:
        print(
            "ha I'm sorry but this password name is not validated it may crash the program (please do not put a space)...")
        time.sleep(2.5)
        error()
    file.write(name_passewod + "=")
    for i in range(12):
        passeword = (hm[random.randint(0, len(hm) - 1)] + HM[random.randint(0, len(hm) - 1)])
        file.write(str(passeword))
    file.write("\n")
    print("your passwords has been registered under the name of : ", name_passewod)
    file.close()
    logging.info("INFO: the \"backup\" function was called")
    src = r"C:\ProgramData\passworld_loggepy\passewords"
    backup_passeword = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy\passewords_back"
    shutil.copy(src, backup_passeword)
    restart()


while True:
    if keyboard.is_pressed("w"):
        logging.info("INFO: user to press \"w\"")
        logging.info(
            "INFO: the user called the function \"passeword_generet\" in this path \"C:\Program Files (x86)\loggepy\Script/loggepy.py\" ")
        passeword_generet()

    if keyboard.is_pressed("r"):
        logging.info("INFO: user to press \"r\"")
        logging.info(
            "INFO: the user called the function \"get_passeword\" in this path \"C:\Program Files (x86)\loggepy\Script/getpasseword.py\" ")
        get_passeword()

    if keyboard.is_pressed("a"):
        logging.info("INFO: user to press \"a\"")
        logging.info(
            "INFO: the user called the function \"add_password\" in this path \"C:\Program Files (x86)\loggepy\Script/addpassword.py\" ")
        add_password()

    if keyboard.is_pressed("e"):
        logging.info("INFO: user to press \"e\"")
        print(Fade.Vertical(Colors.blue_to_green, thank))
        time.sleep(3)
        exit()

    if keyboard.is_pressed("p"):
        logging.info("INFO: user to press \"p\"")
        logging.info(
            "INFO: the user called the function \"all_passeword\" in this path \"C:\Program Files (x86)\loggepy\Script/getpasseword.py\" ")
        get_all_passeword()
        time.sleep(1.5)

    if keyboard.is_pressed("c"):
        logging.info("INFO: user to press \"c\"")
        logging.info(
            "INFO: the user called the function \"copy\" in this path \"C:\Program Files (x86)\loggepy\Script/getpasseword.py\" ")
        copy()

    if keyboard.is_pressed("b"):
        logging.info("INFO: user to press \"b\"")
        logging.info(
            "INFO: the user called the function \"repair\" in this path \"C:\Program Files (x86)\loggepy\Script/repaired.py\" ")
        repair()
        time.sleep(1.5)

    if keyboard.is_pressed("i"):
        logging.info("INFO: user to press \"i\"")
        logging.info("INFO: user requested more info ")
        print(f'\nto generate a password press "w",loggepy will generate an unbreakable password for you, you just gave your password a name to find it later, be careful not to put spaces !!!!! \nto read a password press "r, to read one of your passwords, just press "r" and enter the name of your password, el loggepy will give it to you. be careful not to put spaces !!!!! \nto create a password press "a",this function will allow you to save a password in loggepy (you will therefore have to specify to loggepy the name of the password and the password in luis itself) \nto exit plesse press "e" , this function just left loggepy correctly it is advisable to close it in this way and not with the cross of the window \nto see all your passwords press "p", this function is to see all of these passwords \nto copy your word press "c" , if you press "c" you will no longer be able to enter the name of your password and it will automatically be put in your clipboard and you can paste it with the shortcut "clrt + v"\nif your ./passewords file is corrupted and you have corrected it, call this function (be careful, this will delete your current file to put the file "C:/Users/{os.getlogin()}/AppData/Roaming/loggepy_backup_passeword/passewords_back" \nto delete a password press "d", this function will delete a password contained in "C:\ProgramData\passworld_loggepy\passewords" you will be asked to put the line where the password is located and it will be deleted \nloggepy will look on github if there is a new update and if it is it will download the latest update and replace the old files with the new ones, it is important to specify that this will not delete any word of passes.')
        time.sleep(2.5)

    if keyboard.is_pressed("d"):
        logging.info("INFO: user to press \"d\"")
        logging.info("INFO: the user called the function \"del_passeword\" in this path \"C:\Program Files (x86)\loggepy\Script/delpasseword.py\" ")
        del_passeword()

    if keyboard.is_pressed("u"):
        logging.info("INFO: user to press \"u\"")
        logging.info("INFO: the user called the function \"get_update\" in this path \"C:\Program Files (x86)\loggepy\Script/update.py\"")
        get_update()
        time.sleep(3)
# mettre un mot de passe pour voir l'ensemble des nom de mot de passe a faire a la toute fin du project
