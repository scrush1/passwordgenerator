import random
from os import system
import pyfiglet

H = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
R = "1234567890"
I = "!@#$%^&*().,"

herf = list(H)
reqem = list(R)
isare = list(I)

password = []
pass_str = ""
giris = pyfiglet.figlet_format("PASSWORD GENERATOR")
print(giris)
herf_say = int(input("Herflerin sayini secin :"))
reqem_say = int(input("Reqemlerin sayini secin :"))
isare_say = int(input("Isarenin sayini secin :"))
a = 0
e = 0
c = 0
while True:
    a += 1
    h = random.choice(herf)
    password += h
    if a == herf_say:
        break

while True:
    e +=1
    r = random.choice(reqem)
    password += r
    if e == reqem_say:
        break

while True:

    if c == isare_say or isare_say ==0:
        break
    c += 1
    i = random.choice(isare)
    password += i

for f in password:
    pass_str += f

print("Sifreniz : {}".format(pass_str))
