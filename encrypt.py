from operator import length_hint
from code import encChr

def enc(nameFile):
    #Content Count
    print("[+] Process : Content Count Length")
    file = open(nameFile, 'r')
    contentsLen = length_hint(file.read())
    file.close()

    #Encrypt
    print("[+] Process : Content Encrypt")
    result = ""
    i = 0
    for i in range(contentsLen):
        file = open(nameFile, 'r')
        con = str(encChr(file.read()[i]))
        if length_hint(con) >= 3:
            result = result + "-"+con+"-"
        else:
            result = result + con
        file.close()

    # Output
    print("[+] Process : Make File Encrypt")
    lenNameFile = length_hint(nameFile) - 4
    nameOutputFile = ""
    i = 0
    for i in range(lenNameFile):
        nameOutputFile = nameOutputFile + nameFile[i]
    output = nameOutputFile+"-encrypt.txt"
    fileOutput = open(output, 'w')
    fileOutput.write(result)
    fileOutput.close
    print("[+] Process : Encrypt Success")