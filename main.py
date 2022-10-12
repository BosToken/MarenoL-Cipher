from decrypt import dec
from encrypt import enc


#Input 

# user_choose = str(input('1. Encryption\n2. Decryption\nChoose : '))
# user_input = str(input('[+] Enter Your [txt] File : '))

try:
    
    #Input 
    user_choose = int(input('1. Encryption\n2. Decryption\n\nChoose : '))

    if(user_choose == 1):
        user_input = str(input('[+] Enter Your [txt] File to Encryption : '))
        enc(user_input)

    if(user_choose == 2):
        user_input = str(input('[+] Enter Your [txt] File to Decryption : '))
        dec(user_input)

    file = open(user_input)
    file.close
except FileNotFoundError:
    print("File '"+user_input+"' Not Found")