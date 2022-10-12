from operator import length_hint
from code import decChr

def dec(nameFile):
    # Output
    print("[+] Process : Make File Decrypt")
    lenNameFile = length_hint(nameFile) - 4
    nameOutputFile = ""
    i = 0
    for i in range(lenNameFile):
        nameOutputFile = nameOutputFile + nameFile[i]
    output = nameOutputFile+"-decrypt.txt"
    fileOutput = open(output, 'w')
    fileOutput.close

    #Line Count
    print("[+] Process : Line Count Length")
    file = open(nameFile, 'r')
    countLine = len(file.readlines())
    file.close()
    
    #Content Count
    print("[+] Process : Count Content Length")
    contentsLen = 0
    index = 0
    for index in range(countLine):
        file = open(nameFile, 'r')
        contentsLen = length_hint(file.readlines()[index])
        if(index == countLine - 1):
            contentsLen = contentsLen
        else:
            contentsLen = contentsLen - 1
        file.close()

        #Decrypt Line
        index2 = 0
        l = 0
        r = 1
        finalResut = ""
        for index2 in range(contentsLen // 2):
            #Left Byte
            file = open(nameFile, 'r')
            resultL = file.readlines()[index][l]
            file.close
            
            #Right Byte
            file = open(nameFile, 'r')
            resultR = file.readlines()[index][r]
            file.close

            #Final Result
            finalResut = resultL+resultR
            l = l + 2
            r = r + 2
            file = open(output, 'a')
            file.write(decChr(finalResut))
            file.close()
        
        if(index == countLine - 1):
            IDK = ""
        else:
            file = open(output, 'a')
            file.write("\n")
            file.close()
    print("[+] Process : Decrypt Success")