



uni= []
parenCount=0
keyCount=0
def read_AF(t): 
    global parenCount, keyCount
    isGood = True
    word = ''
    for i in range(len(t)):
        
        word += t[i]
        print(word, isGood)
        
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
        if word == 'while' and parenCount%2==0 and keyCount%2==0 : 
            word = ''
            print('understood')
        if word == 'do' and parenCount%2==0 and keyCount%2==0 : 
            word = ''
            print('understood')
        if t == '':
            print('understood')
            return True 
        if word == 'walk' or 'free' or 'drop':
            word == ''
            print('understood')
    print("wtf")
    if parenCount%2>0 or keyCount%2>0 : 
        print('got it')
        isGood=False
    if word != '':
        print("I don't get it")
        isGood =False
    return isGood, keyCount,parenCount
            

        
def readInitEnd(t):
    global isGood
    if "GORP" in t and "PROG" in t:
        isGood = True
    else:
        isGood = False

def main():
    global isGood
    t = input("Ingrese el programa: ")
    isOk = read_AF(t)
    print(isOk)
    

main()
    
