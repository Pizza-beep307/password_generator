import random
from letter_generator import *
from integer_generator import *
from symbols_generator import *

def main():
    print("Quelle taille de mot de passe souhaitez vous :")

    pwd_length = int(input('Taille:'))
    password = ""

    for i in range(pwd_length):
        num = random.randint(0, 2)
        if num == 0:
            password += random_letter()
        elif num == 1:
            password += random_integer()
        else:
            password += random_symbols()
    
    print(password)

main()




