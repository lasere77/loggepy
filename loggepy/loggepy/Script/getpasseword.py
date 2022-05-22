import logging
import os

from dotenv import load_dotenv
import pyperclip as pc


def get_passeword():
    logging.info('INFO: the user called the function "get_passeword"')
    choose = input("please enter the name of your password : ")
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    print(os.getenv(choose))


def get_all_passeword():
    logging.info('INFO: the user called the function "all_passeword"')
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    file = open("C:\ProgramData\passworld_loggepy\passewords", "r")
    print("all of your passwords are :")
    print("\n" + file.read())


def copy():
    logging.info('INFO: the user called the function "copy"')
    choose = input("please put the name of your password that you want to copy : ")
    load_dotenv(dotenv_path="C:\ProgramData\passworld_loggepy/passewords")
    print(os.getenv(choose) + " was copied")
    pc.copy(os.getenv(choose))
