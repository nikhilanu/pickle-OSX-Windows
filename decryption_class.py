import concode

class decryption:
#--------------------------------------------------------------------------#

    def __init__(self):
                self.decrypted_message=""
                f1=open("encrypted message.txt","r")
                self.encrypted_message=f1.read()
                f1.close()
#--------------------------------------------------------------------------#

    def d_password(self):
                self.pass_code = input("Enter your password : ")
                self.pass_code = concode.userpass(self.pass_code)

#--------------------------------------------------------------------------#

    def decrypting(self):
                self.code_string = str(self.pass_code)
                x = -1
                for i in range (0,len(self.encrypted_message)):
                                    if i%(len(self.code_string)) == 0:
                                        x += 1
                                    self.decrypted_message += unichr( ord( self.encrypted_message[i] ) - int(self.code_string[i-((len(self.code_string))*x)]) )
#--------------------------------------------------------------------------#

    def decryptedfile(self):
        f2=open("decrypted message.txt","w")
        f2.write(self.decrypted_message)
        f2.close()
#---------------------------end of class----------------------------------#

obj2=decryption()
obj2.d_password()
obj2.decrypting()
obj2.decryptedfile()
print "decrypted_message has been created"

    
