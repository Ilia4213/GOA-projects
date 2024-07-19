from random import *

print('Here we will generate you strong passwords.')

pass_len = input('Please enter your password length, type "Close" to exit:')

pass_len = pass_len.lower()

old_password = ""

while str(pass_len) != "close":

    password = ""

    try:
        if int(pass_len) > 4 and int(pass_len) < 11:
            
            characters = "@6*%2&3$18>5+/470-_ceafvk"  
            
            while len(password) < int(pass_len):
                password += choice(characters)

            if password != old_password:
                print("Generated password:", password)
                pass_len = input('Please enter your password length:')    
                pass_len = pass_len.lower()
                old_password = password
            else:
                print("")

        else:
            pass_len = input('Lenght should be from 5 to 10, enter again or type "Close" to exit:')
            pass_len = pass_len.lower()
    except ValueError:
        pass_len = input('Invalid input. Please enter a valid number or "Close" to exit: ')
        pass_len = pass_len.lower()

print("Closing the program...")    
