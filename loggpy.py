from getpasseword import get_passeword

import string
from dotenv import load_dotenv
import random
import os

load_dotenv(dotenv_path="passeworld/passewords")

hm = list(string.ascii_lowercase)
HM = list(string.ascii_uppercase)
file = open("passeworld/passewords", "a+")

write_passewod = input("voullez vous créer un mot de passe ?")
read_passewod = input("voulez vous lire votre mot de passe ?")


def passeword_generet():
    print(file.read())
    name_passewod = input("name of passeword : ")
    file.write(name_passewod + "=")
    for i in range(15):
        passeword = hm[random.randint(0, len(hm) - 1)]
        file.write(passeword)
    file.write("\n")

if write_passewod == "1":
    passeword_generet()


if read_passewod == "1":
    get_passeword()

#mettre un mot de passe pour voir l'ensemble des nom de mot de passe

#récupérer le nom des mot de passe
