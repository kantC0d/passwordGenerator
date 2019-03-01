#this project is using Python 3.6.1
import random
import subprocess

#printable char list
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

#get password length
passwordLength = input("\nPassword Length: ")

#detect if the password length input is an int, if not, ask again
while type(passwordLength) != int:
    #try to change the type of password into an int
    try:
        int(passwordLength)
        #detect if the password length is less or equal to 0
        if int(passwordLength) <= 0:
            passwordLength = input("\nEnter a valid Password Length: ")
        else:
            int(passwordLength)
            break

    #in case it doesn't work, it asks the question again
    except:
        passwordLength = input("\nEnter a valid Password Length: ")

#
print("\nPassword Length >> " + passwordLength)


#generate password string
passwordLength = int(passwordLength)
password = ""

for char in range(0, passwordLength):
    password += random.choice(printable)

#print the password
print("\n\nYour password is: \n" + password)


