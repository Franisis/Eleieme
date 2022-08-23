isGood = False
uni= []
parenCount=0
keyCount=0
def read_AF(t): 

    word = ''
    for i in range(len(t)):
        
        word += t[i]
        print(word)
        if " " in word:
            word = ''
        if word == "vars" and ";" in t:
            word = ""
            print("understood")
        if word == "prog".upper() and "prog".upper() not in uni:
            uni.append(word)
            word = ""
            print("understood")
        if word == "gorp".upper() and "gorp".upper() not in uni:
            uni.append(word)
            word = ""
            print("understood")
        if word == 'if' and "fi" in t:
            word = ''
            print("undesrtood")
        if word == 'PROC':
            word  = ''
            print ("understood")
        if t[i] == '(' or t[i] == ')':
            parenCount+=1
        if t[i] == '{' or t[i] == '}':
            keyCount+=1     
        
def readInitEnd(t):
    global isGood
    if "GORP" in t and "PROG" in t:
        isGood = True
    else:
        isGood = False

def main():
    global isGood
    t = input("Ingrese el programa: ")
    readInitEnd(t)
    read_AF(t)
main()
    
