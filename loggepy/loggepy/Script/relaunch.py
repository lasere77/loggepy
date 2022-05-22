import os
import logging

import time


def restart():
    logging.info("INFO: the program will restart.")
    print("the program had to stop for the proper functioning of the programe. ")
    time.sleep(2.5)
    os.chdir(r"C:\Program Files (x86)\loggepy")
    os.system("launcher.bat")
    error()


def error():
    logging.error("FATAL: the program had to stop ")
    exit()
