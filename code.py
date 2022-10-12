def encChr(chr):

    #Upper
    if(chr == "A"):
        return "A0"
    elif(chr == "B"):
        return "C0"
    elif(chr == "C"):
        return "E0"
    elif(chr == "D"):
        return "G0"
    elif(chr == "E"):
        return "I0"
    elif(chr == "F"):
        return "K0"
    elif(chr == "G"):
        return "M0"
    elif(chr == "H"):
        return "O0"
    elif(chr == "I"):
        return "Q0"
    elif(chr == "J"):
        return "S0"
    elif(chr == "K"):
        return "U0"
    elif(chr == "L"):
        return "W0"
    elif(chr == "M"):
        return "Y0"
    elif(chr == "N"):
        return "Z0"
    elif(chr == "O"):
        return "X0"
    elif(chr == "P"):
        return "V0"
    elif(chr == "Q"):
        return "T0"
    elif(chr == "R"):
        return "R0"
    elif(chr == "S"):
        return "P0"
    elif(chr == "T"):
        return "N0"
    elif(chr == "U"):
        return "L0"
    elif(chr == "V"):
        return "J0"
    elif(chr == "W"):
        return "H0"
    elif(chr == "X"):
        return "F0"
    elif(chr == "Y"):
        return "D0"
    elif(chr == "Z"):
        return "B0"

    #Lower
    elif(chr == "a"):
        return "0B"
    elif(chr == "b"):
        return "0D"
    elif(chr == "c"):
        return "0F"
    elif(chr == "d"):
        return "0H"
    elif(chr == "e"):
        return "0J"
    elif(chr == "f"):
        return "0L"
    elif(chr == "g"):
        return "0N"
    elif(chr == "h"):
        return "0P"
    elif(chr == "i"):
        return "0R"
    elif(chr == "j"):
        return "0T"
    elif(chr == "k"):
        return "0V"
    elif(chr == "l"):
        return "0X"
    elif(chr == "m"):
        return "0Z"
    elif(chr == "n"):
        return "0Y"
    elif(chr == "o"):
        return "0W"
    elif(chr == "p"):
        return "0U"
    elif(chr == "q"):
        return "0S"
    elif(chr == "r"):
        return "0Q"
    elif(chr == "s"):
        return "0O"
    elif(chr == "t"):
        return "0M"
    elif(chr == "u"):
        return "0K"
    elif(chr == "v"):
        return "0I"
    elif(chr == "w"):
        return "0G"
    elif(chr == "x"):
        return "0E"
    elif(chr == "y"):
        return "0C"
    elif(chr == "z"):
        return "0A"

    #Number
    elif(chr == "1"):
        return "ZZ"
    elif(chr == "2"):
        return "YY"
    elif(chr == "3"):
        return "XX"
    elif(chr == "4"):
        return "WW"
    elif(chr == "5"):
        return "VV"
    elif(chr == "6"):
        return "EE"
    elif(chr == "7"):
        return "DD"
    elif(chr == "8"):
        return "CC"
    elif(chr == "9"):
        return "BB"
    elif(chr == "0"):
        return "AA"

    #Symbol
    elif(chr == "!"):
        return "1B"
    elif(chr == "#"):
        return "1D"
    elif(chr == "$"):
        return "1F"
    elif(chr == "%"):
        return "1H"
    elif(chr == "&"):
        return "1J"
    elif(chr == "("):
        return "1L"
    elif(chr == ")"):
        return "1N"
    elif(chr == "*"):
        return "1P"
    elif(chr == "+"):
        return "1R"
    elif(chr == ","):
        return "1T"
    elif(chr == "-"):
        return "1W"
    elif(chr == "."):
        return "1Y"
    elif(chr == "/"):
        return "A1"
    elif(chr == " "):
        return "B1"
    elif(chr == ":"):
        return "Z1"
    elif(chr == ";"):
        return "1Z"
    elif(chr == "<"):
        return "1X"
    elif(chr == "="):
        return "1U"
    elif(chr == ">"):
        return "1S"
    elif(chr == "@"):
        return "1Q"
    elif(chr == "["):
        return "1O"
    elif(chr == "]"):
        return "1M"
    elif(chr == "^"):
        return "1K"
    elif(chr == "_"):
        return "1I"
    elif(chr == "{"):
        return "1G"
    elif(chr == "}"):
        return "1E"
    elif(chr == "|"):
        return "1C"
    elif(chr == "~"):
        return "1A"
    else:
        return " "+chr
    

def decChr(chr):

    #Upper
    if(chr == "A0"):
        return "A"
    elif(chr == "C0"):
        return "B"
    elif(chr == "E0"):
        return "C"
    elif(chr == "G0"):
        return "D"
    elif(chr == "I0"):
        return "E"
    elif(chr == "K0"):
        return "F"
    elif(chr == "M0"):
        return "G"
    elif(chr == "O0"):
        return "H"
    elif(chr == "Q0"):
        return "I"
    elif(chr == "S0"):
        return "J"
    elif(chr == "U0"):
        return "K"
    elif(chr == "W0"):
        return "L"
    elif(chr == "Y0"):
        return "M"
    elif(chr == "Z0"):
        return "N"
    elif(chr == "X0"):
        return "O"
    elif(chr == "V0"):
        return "P"
    elif(chr == "T0"):
        return "Q"
    elif(chr == "R0"):
        return "R"
    elif(chr == "P0"):
        return "S"
    elif(chr == "N0"):
        return "T"
    elif(chr == "L0"):
        return "U"
    elif(chr == "J0"):
        return "V"
    elif(chr == "H0"):
        return "W"
    elif(chr == "F0"):
        return "X"
    elif(chr == "D0"):
        return "Y"
    elif(chr == "B0"):
        return "Z"

    #Lower
    elif(chr == "0B"):
        return "a"
    elif(chr == "0D"):
        return "b"
    elif(chr == "0F"):
        return "c"
    elif(chr == "0H"):
        return "d"
    elif(chr == "0J"):
        return "e"
    elif(chr == "0L"):
        return "f"
    elif(chr == "0N"):
        return "g"
    elif(chr == "0P"):
        return "h"
    elif(chr == "0R"):
        return "i"
    elif(chr == "0T"):
        return "j"
    elif(chr == "0V"):
        return "k"
    elif(chr == "0X"):
        return "l"
    elif(chr == "0Z"):
        return "m"
    elif(chr == "0Y"):
        return "n"
    elif(chr == "0W"):
        return "o"
    elif(chr == "0U"):
        return "p"
    elif(chr == "0S"):
        return "q"
    elif(chr == "0Q"):
        return "r"
    elif(chr == "0O"):
        return "s"
    elif(chr == "0M"):
        return "t"
    elif(chr == "0K"):
        return "u"
    elif(chr == "0I"):
        return "v"
    elif(chr == "0G"):
        return "w"
    elif(chr == "0E"):
        return "x"
    elif(chr == "0C"):
        return "y"
    elif(chr == "0A"):
        return "z"

    #Number
    elif(chr == "ZZ"):
        return "1"
    elif(chr == "YY"):
        return "2"
    elif(chr == "XX"):
        return "3"
    elif(chr == "WW"):
        return "4"
    elif(chr == "VV"):
        return "5"
    elif(chr == "EE"):
        return "6"
    elif(chr == "DD"):
        return "7"
    elif(chr == "CC"):
        return "8"
    elif(chr == "BB"):
        return "9"
    elif(chr == "AA"):
        return "0"

    #Symbol
    elif(chr == "1B"):
        return "!"
    elif(chr == "1D"):
        return "#"
    elif(chr == "1F"):
        return "$"
    elif(chr == "1H"):
        return "%"
    elif(chr == "1J"):
        return "&"
    elif(chr == "1L"):
        return "("
    elif(chr == "1N"):
        return ")"
    elif(chr == "1P"):
        return "*"
    elif(chr == "1R"):
        return "+"
    elif(chr == "1T"):
        return ","
    elif(chr == "1W"):
        return "-"
    elif(chr == "1Y"):
        return "."
    elif(chr == "A1"):
        return "/"
    elif(chr == "B1"):
        return " "
    elif(chr == "Z1"):
        return ":"
    elif(chr == "1Z"):
        return ";"
    elif(chr == "1X"):
        return "<"
    elif(chr == "1U"):
        return "="
    elif(chr == "1S"):
        return ">"
    elif(chr == "1Q"):
        return "@"
    elif(chr == "1O"):
        return "["
    elif(chr == "1M"):
        return "]"
    elif(chr == "1K"):
        return "^"
    elif(chr == "1I"):
        return "_"
    elif(chr == "1G"):
        return "{"
    elif(chr == "1E"):
        return "}"
    elif(chr == "1C"):
        return "|"
    elif(chr == "1A"):
        return "~"
    else:
        return chr[1]