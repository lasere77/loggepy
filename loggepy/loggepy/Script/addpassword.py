import logging

from dotenv import load_dotenv
import os
import shutil
import time

from relaunch import restart


def add_password():
    logging.info('INFO: the user called the function "add_passeword"')
    choose_name = input("please enter the name of your password : ")
    choose_addPassword = input(f"please put the password whose name is {choose_name} : ")
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    file = open("C:\ProgramData\passworld_loggepy\passewords", "a+")
    if " " in choose_name:
        print("ha I'm sorry but this password name is not validated it may crash the program (please do not put a space)...")
        time.sleep(2.5)
        restart()
    if choose_name == "":
        print("ha I'm sorry but this password name is not validated it may crash the program (Please put arguments )...")
        time.sleep(2.5)
        restart()
    file.write(choose_name + "=" + choose_addPassword)
    file.write("\n")
    print(f"your password has been saved as {choose_name} with as password {choose_addPassword}")
    file.close()
    logging.info("INFO: the \"backup\" function was called")
    src = r"C:\ProgramData\passworld_loggepy\passewords"
    backup_passeword = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy\passewords_back"
    shutil.copy(src, backup_passeword)
    restart()
