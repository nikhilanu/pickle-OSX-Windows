print "© 2016 NIKHIL & NITHIN ALL RIGHTS RESERVED"
print """======================
| Welcome to PICKLE |
======================
"""

print """Press:
S to start using the program
A for About
X to exit
"""

while True:
    ch1 = raw_input ("Enter option: ")

    if ch1 == "S":
        choice = 1
        break

    elif ch1 == "A":
        print """Pickle is an encryption program that allows you to encrypt data that you want secured and hidden from someone else.
Rosetta allows you to encrypt your data using a password that you may choose yourself or one that is generated at random by the AI.
Data encrypted using Rosetta can not be decrypted without Rosetta and the password.
The password is also encrypted for added security.
"""
        continue

    elif ch1 == "X":
        choice = -1
        print "You are exiting Pickle."
        break

while choice>0:
    print
    choice=raw_input("Enter E for encryption or D for decryption : ")
    print
    if choice=="E":
        import encryption_class
    elif choice=="D":
        import decryption_class

