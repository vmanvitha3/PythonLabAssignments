#My UMKC web Application
#password validation against database rules using loops
import re   #import regular expressions

#function to validate password against rules and print result
def validatePassword(passwd):
    if(len(passwd))<6 or (len(passwd)>16):  #check if password length doesn't lie with the range of 6 and 16
        print("Password length should be in the range 6-16 characters")
        return False                        #if it doesn't lie return False
    elif re.search('[A-Z]',passwd) is None: #check if passwd doesn't have atleast one uppercase character
        print("Password should have atleast one uppercase character")
        return False                        #if it doesn't then return False
    elif re.search('[a-z]',passwd) is None: #check if passwd doesn't have atleast one lowercase character
        print("Password should have atleast one lowercase character")
        return False                        #if it doesn't then return False
    elif re.search('[0-9]', passwd) is None:#check if passwd doesn't have atleast one number
        print("Password should have atleast one number")
        return False                        #if it doesn't then return False
    elif re.search('[$@!*]',passwd) is None:#check if passwd doesn't have atleast one special character
        print("Password should have atleast one special character from the set [$@!*]")
        return False                        #if it doesn't then return False
    else:                   #if passwd follows all rules it returns True and exits the program
        print("Password is Valid")
        return True

#Program starts here
checkPasswd = False                             #set checkPasswd to False

while not checkPasswd:                          #if not a valid password it asks to re enter password
    passwd = input("Enter password: ")      #user enters password
    checkPasswd = validatePassword(passwd)  #call validate password function to check if it is a valid password