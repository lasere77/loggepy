import os
import shutil
import logging


def repair():
    logging.info("INFO: the \"repair\" function was called")
    backup_file_passewords = rf"C:\Users\{os.getlogin()}\AppData\Roaming\loggepy\passewords_back"
    passewords_file = r"C:\ProgramData\passworld_loggepy\passewords"
    shutil.copy(backup_file_passewords, passewords_file)
    print("your password file has been successfully changed")

