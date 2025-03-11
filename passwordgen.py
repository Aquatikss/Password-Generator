import random

uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = uppers.lower()
digits = "0123456789"
symbols = "!@#$%^&*()-_=+[{]}|;:,<.>/?\\ "

uppersBool = True
lowersBool = True
digitsBool = True
symbolsBool = True

all = ""

password = ""

if uppersBool == True:
    all += uppers

if lowersBool == True:
    all += lowers

if digitsBool == True:
    all += digits

if symbolsBool == True:
    all += symbols

length = int(input("Enter the desired password length: "))

for i in range (length):
    password += random.choice(all)

print(password)

breakLoop = bool(input("Type to exit: "))