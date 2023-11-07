#OTP

def one_pad(text, key, type, function):
    alp = list("abcdefghijklmnopqrstuvwxyz")
    ans = ''
    for i in range(len(text)):
        if text[i] == " ":ans += " "
        if function == 1:
            if type == 1:
                ans += alp[(alp.index(text[i]) + alp.index(key[i])) % 26].upper()
            elif type == 2:
                ans += alp[(alp.index(text[i]) - alp.index(key[i])) % 26]
        if function == 2:
            if text[i] == key[i]:ans += "0"
            else:ans += '1'
    return ans

while True:
    print("***OTP***")
    print("1.Using alphabets")
    print("2.Using Xor ")
    print("3.Exit")
    function = int(input("Enter choice(1/2/3) :  "))
    if function == 3: break
    while True:
            text = input("Enter the text: ").lower()
            key = input("Enter the key: ").lower()
            print("1.Encryption")
            print("2.Decryption")
            type = int(input("> "))
            print(one_pad(text, key, type, function))
            if input("Do you want to continue (y/n): ") == 'n': break


#------------------------------------------------------------------

#OTP

def one_pad(text, key, type, function):
    alp = list("abcdefghijklmnopqrstuvwxyz")
    ans = ''
    for i in range(len(text)):
        if text[i] == " ":ans += " "
        if function == 1:
            if type == 1:
                ans += alp[(alp.index(text[i]) + alp.index(key[i])) % 26].upper()
            elif type == 2:
                ans += alp[(alp.index(text[i]) - alp.index(key[i])) % 26]
        if function == 2:
            if text[i] == key[i]:ans += "0"
            else:ans += '1'
    return ans
numbers="123456789"
alpha="abcdefghijklmnopqrstuvwxyz"
while True:
    print("***OTP***")
    print("1.Using alphabets")
    print("2.Using Xor ")
    print("3.Exit")
    function = int(input("Enter choice(1/2/3) :  "))
    if function == 3: break
    while True:
        if function==1:
            text = input("Enter the text: ").lower()
            key = input("Enter the key: ").lower()
            for i in numbers:
                if (i  in text) or (i  in key):
                    print("Invalid String!!")
                    break
            text = input("Enter the text: ").lower()
            key = input("Enter the key: ").lower()
            if len(text)==len(key):
                        print("1.Encryption")
                        print("2.Decryption")
                        type = int(input("> "))
                        print(one_pad(text, key, type, function))
                        if input("Do you want to continue (y/n): ") == 'n': break

            else:
                        print("Length of text should be equal to length of key !!")
        if function==2:

                text = input("Enter the text: ").lower()
                key = input("Enter the key: ").lower()
                for i in alpha:
                    if (i  in text) or (i  in key):
                        print("Invalid binary!!")
                        break
                        
                text = input("Enter the text: ").lower()
                key = input("Enter the key: ").lower()
                if len(text) == len(key):
                    print("1.Encryption")
                    print("2.Decryption")
                    type = int(input("> "))
                    print(one_pad(text, key, type, function))
                    if input("Do you want to continue (y/n): ") == 'n': break

                else:
                    print("Length of text should be equal to length of key !!")
