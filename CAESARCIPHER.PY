#caesar cipher 

def con1():
    decision=input("Continue..? (y/n) : ")
    if decision.lower()=="y":
        print(">> 1. Using Mathematical Expression ")
        m()
    elif decision.lower()=="n":
        pass
    else:
        print("Invalid option!!")
        return con1()

def con2():
    decision = input("Continue..? (y/n) : ")
    if decision.lower() == "y":
        print(">> 2. Without using MAthematical Expression ")
        nm()
    elif decision.lower()=="n":
        pass
    else:
        print("Invalid option!!")
        return con2()

def en(text,key):
    cipher=""
    for i in text:
        if i==" ": cipher+=i
        elif i.isupper():cipher+=chr((ord(i)+key-65)%26+65)
        else: cipher+=chr((ord(i)+key-97)%26+97)
    return cipher.upper()
def de(text,key):
    original=""
    for i in text:
        if i==" ":original+=i
        elif i.isupper():
            chr((ord(i) - key - 65) % 26 + 65)
        else:
            original += chr((ord(i) - key - 97) % 26 + 97)
    return original
def homepage():
    ch = input("Go to Home Page..? (y/n) : ")
    if ch.lower() == "y":
        pass
    elif ch.lower() == "n":
        exit()
    else:
        print("Invalid Choice!!!")
        return homepage()
def m():
    print('''
           1. Encryption
           2. Decryption''')
    choice = int(input("Enter your Choice (1/2) : "))
    if choice == 1:
        text = input("Enter Text : ")
        shift = int(input("Enter Shift Key : "))
        print("Encrypted Text : ")
        print(en(text, shift))
    elif choice == 2:
        text = input("Enter Encrypted Text : ")
        shift = int(input("Enter the Shift Key : "))
        print("Decrypted Text : ")
        print(de(text, shift))
    else:
        print("Invalid Option")
        return m()
    return con1()
    
def nm():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print('''
                   1. Encryption
                   2. Decryption''')
    u2 = input("Enter Choice(1/2) : ")
    if u2 == "1":
        text = input("Enter Text : ")
        key = int(input("Key : "))
        print("Encrypted Text : ")
        cipher = ""
        for i in text:
            in_dex = alphabet.index(i)
            result = in_dex + key
            if result > 25:
                result = result - 26
                cipher += alphabet[result].upper()
            else:
                cipher += alphabet[result].upper()
        print(cipher)

    elif u2 == "2":
        text = input("Enter Encrypted Text : ")
        key = int(input("Key : "))
        print("Decrypted Text : ")
        cipher = ""
        for i in text:
            in_dex = alphabet.index(i)
            result = in_dex - key
            cipher += alphabet[result].lower()
        print(cipher)
    else:
        print("Invalid Choice!!")
        return nm()
    return con2()


while True:
    print("*** Caesar Cipher ***")
    print('''
    1. Using Mathematical Expression
    2. Without using Mathematical Expression''')
    u1=input("Enter Choice (1/2) : ")
    if u1.lower()=="1":
        m()

    elif u1.lower()=="2":
        nm()
    else:
        print("Invalid CHoice!!")
    homepage()



