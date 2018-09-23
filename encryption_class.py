class encryption:
#--------------------------------------------------------------------------#
    def __init__(self):
        self.raw_message=raw_input("""Enter your message for encryption:
""")
        self.encrypted_message=""

#--------------------------------------------------------------------------#

    def password(self):
        import random
                
        self.password_type=input("""
Enter:
1 for user defined password
2 for auto generated password
""")
        if self.password_type==1:
            self.pass_code=input("PASSWORD:  ")

        else:
            self.pass_code = random.randint(10000,100000)
            print self.pass_code
            
#--------------------------------------------------------------------------#

    def encrypting(self):
        import concode
        self.code_string = str(concode.userpass(self.pass_code))
        x = -1


        for i in range (0,len(self.raw_message)):
                            if i%(len(self.code_string)) == 0:
                                x += 1
                            self.encrypted_message += unichr( ord( self.raw_message[i] ) + int(self.code_string[i-((len(self.code_string))*x)]) )
  
#--------------------------------------------------------------------------#
    def encryptedfile(self):
        f1=open("encrypted message.txt","w")
        f1.write(self.encrypted_message)
        f1.close()

#---------------------------main program-----------------------------------#

obj1=encryption()
obj1.password()
obj1.encrypting()
obj1.encryptedfile()
print "encrypted_message has been created"
