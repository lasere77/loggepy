import logging

import keyboard
from dotenv import load_dotenv
from relaunch import restart
from getpasseword import get_all_passeword


def del_passeword():
    logging.info('INFO: the user called the function "add_passeword"')
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    get_all_passeword()
    choose_ligne = int(input("please put the line where the password you want to delete is located : "))
    file = open("C:\ProgramData\passworld_loggepy\passewords", "r")
    what_password = file.readlines(choose_ligne)
    file.close()
    print(f"you are about to delete the password: {str(what_password)} ? if you are sure remove this password, please press 'y' if you are not sure, please press 'n' : ")
    while True:
        if keyboard.is_pressed("y"):
            file = open("C:\ProgramData\passworld_loggepy\passewords", "r")
            lignes = file.readlines()
            file.close()
            lignes[choose_ligne - 1] = ""
            file = open("C:\ProgramData\passworld_loggepy\passewords", "w")
            file.writelines(lignes)
            file.close()
            logging.info(f'INFO: the user del ligne {choose_ligne}')
            print(f"your password on the line {choose_ligne} has been deleted ")
            restart()
        elif keyboard.is_pressed("n"):
            restart()
