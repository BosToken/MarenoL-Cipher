from decrypt import dec
from encrypt import enc

#Input 
user_input = str(input('[+] Enter Your [txt] File : '))

try:
    file = open(user_input)
    file.close
    enc(user_input)
    # dec(user_input)
except FileNotFoundError:
    print("File '"+user_input+"' Not Found")