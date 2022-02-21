from dotenv import load_dotenv
import os


def get_passeword():
    choose = input("merci de mettre le nom de votre mot de passe : ")
    load_dotenv(dotenv_path="passeworld/passewords")
    print(os.getenv(choose))